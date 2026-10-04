import errata from '../data/errata.json';

type MarkdownNode = {
  type: string;
  url?: string;
  value?: string;
  children?: MarkdownNode[];
  data?: { hChildren?: MarkdownNode[] };
};

type Shortcode = { name: 'overrule' | 'wpex'; closing: boolean; more?: string };
type EditorialCorrection = {
  wp_id: number;
  location: string;
  original: string;
  replacement: string;
  reason: string;
  verification_status: string;
};

const localHostnames = new Set(['mathrao.com', 'www.mathrao.com']);

function applyEditorialCorrections(
  value: string,
  corrections: EditorialCorrection[],
  counts: Map<EditorialCorrection, number>,
): string {
  for (const correction of corrections) {
    const occurrences = value.split(correction.original).length - 1;
    if (occurrences) {
      counts.set(correction, (counts.get(correction) || 0) + occurrences);
      value = value.replaceAll(correction.original, correction.replacement);
    }
  }
  return value;
}

function localSiteUrl(value: string): string {
  if (!/^(?:https?:)?\/\//i.test(value)) return value;

  let url: URL;
  try {
    url = new URL(value.startsWith('//') ? `https:${value}` : value);
  } catch {
    return value;
  }

  if (!localHostnames.has(url.hostname.toLowerCase())) return value;
  return `${url.pathname}${url.search}${url.hash}`;
}

function compatibleEqnarray(value: string): string {
  const start = '\\begin{eqnarray}';
  const end = '\\end{eqnarray}';
  if (value.split(start).length !== 2 || value.split(end).length !== 2) return value;

  if (/&(?:amp;)?\s*=\s*&(?:amp;)?/.test(value)) {
    return value.replace(start, '\\begin{array}{rcl}').replace(end, '\\end{array}');
  }

  if (/\\left\s*\\\{[\s\S]*?\\begin\{array\}/.test(value)) {
    return value.replace(start, '').replace(end, '');
  }

  return value;
}

function transformHtml(value: string): string {
  const compatibleMath = value.replace(
    /\$([^$]*?\\begin\{eqnarray\}[\s\S]*?\\end\{eqnarray\}[^$]*?)\$/g,
    (_whole, formula: string) => `$${compatibleEqnarray(formula)}$`,
  );

  const delimitedMath = compatibleMath.replace(
    /\\begin\{eqnarray\}[\s\S]*?\\end\{eqnarray\}/g,
    (formula) => `$$${compatibleEqnarray(formula)}$$`,
  );

  const withoutEmbeds = delimitedMath.replace(
    /<(?:iframe|object|embed|script|form)\b[^>]*>(?:[\s\S]*?<\/(?:iframe|object|embed|script|form)\s*>)?/gi,
    '<span class="legacy-embed-review">[旧埋め込み]</span>',
  );

  const attributes = withoutEmbeds.replace(
    /\b(src|href|poster)\s*=\s*(["'])(.*?)\2/gi,
    (whole, name: string, quote: string, url: string) => {
      const local = localSiteUrl(url.replace(/&amp;/g, '&'));
      return local === url ? whole : `${name}=${quote}${local.replace(/&/g, '&amp;')}${quote}`;
    },
  );

  return attributes.replace(
    /(?:https?:)?\/\/(?:www\.)?mathrao\.com\/[^\s"'<>]*/gi,
    (url) => localSiteUrl(url),
  );
}

function escapeHtml(value: string): string {
  return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function extractShortcodes(node: MarkdownNode): Shortcode[] {
  const found: Shortcode[] = [];
  if ((node.type === 'text' || node.type === 'html') && node.value) {
    node.value = node.value.replace(
      /\[(\/)?(overrule|wpex)(?:\s+[^\]]*)?\]/gi,
      (token, slash: string | undefined, name: string) => {
        const more = token.match(/\bmore\s*=\s*["'“”‘’]([^"'“”‘’]+)["'“”‘’]/i)?.[1];
        found.push({ name: name.toLowerCase() as Shortcode['name'], closing: Boolean(slash), more });
        return '';
      },
    );
  }
  node.children?.forEach((child) => found.push(...extractShortcodes(child)));
  return found;
}

function shortcodeHtml(code: Shortcode): MarkdownNode {
  if (code.name === 'overrule') {
    return { type: 'html', value: code.closing ? '</aside>' : '<aside class="legacy-overrule">' };
  }
  const label = escapeHtml(code.more || '詳しく見る');
  return { type: 'html', value: code.closing ? '</details>' : `<details class="legacy-wpex"><summary>${label}</summary>` };
}

function renderShortcodes(tree: MarkdownNode): void {
  if (!tree.children) return;

  const output: MarkdownNode[] = [];
  const opened: Shortcode['name'][] = [];

  for (const child of tree.children) {
    const markers = extractShortcodes(child);

    for (const marker of markers.filter((item) => !item.closing)) {
      output.push(shortcodeHtml(marker));
      opened.push(marker.name);
    }

    const empty =
      child.type === 'paragraph' &&
      child.children?.every((item) => item.type === 'text' && !(item.value || '').trim());

    if (!empty) output.push(child);

    for (const marker of markers.filter((item) => item.closing)) {
      if (opened.at(-1) === marker.name) {
        output.push(shortcodeHtml(marker));
        opened.pop();
      }
    }
  }

  tree.children = output;
}

/**
 * Content rendering only.
 * WordPress routing/migration compatibility intentionally does not live here.
 */
export function remarkLegacyMarkdown() {
  return (tree: MarkdownNode, file: { path?: string }) => {
    const sourceName = file.path?.replace(/\\/g, '/').split('/').at(-1) || '';
    const wpId = Number(sourceName.match(/^wp-(\d{6})-/)?.[1]);
    const corrections = (errata as EditorialCorrection[]).filter((entry) => entry.wp_id === wpId);
    const counts = new Map<EditorialCorrection, number>();

    const visit = (node: MarkdownNode): void => {
      if ((node.type === 'math' || node.type === 'inlineMath') && node.value) {
        node.value = applyEditorialCorrections(node.value, corrections, counts)
          .replace(/&gt;/gi, '>')
          .replace(/&lt;/gi, '<')
          .replace(/&amp;/gi, '&');

        node.value = compatibleEqnarray(node.value);

        const mathText =
          node.type === 'math'
            ? node.data?.hChildren?.[0]?.children?.[0]
            : node.data?.hChildren?.[0];

        if (mathText?.type === 'text') mathText.value = node.value;
      }

      if ((node.type === 'image' || node.type === 'link' || node.type === 'definition') && node.url) {
        node.url = localSiteUrl(node.url);
      }

      if (node.type === 'html' && node.value) {
        node.value = transformHtml(applyEditorialCorrections(node.value, corrections, counts));
      }

      node.children?.forEach(visit);
    };

    visit(tree);

    for (const correction of corrections) {
      if (counts.get(correction) !== 1) {
        throw new Error(
          `Editorial correction for WP ${wpId} at ${correction.location} matched ${counts.get(correction) || 0} times (expected 1)`,
        );
      }
    }

    renderShortcodes(tree);
  };
}
