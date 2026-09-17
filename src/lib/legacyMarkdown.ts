import assetMap from '../../migration/asset-map.json';
import sourceIndex from '../../migration/source-index.json';
import slugAliases from '../../migration/slug-aliases.json';
import errata from '../../migration/errata.json';

type MarkdownNode = {
  type: string;
  url?: string;
  value?: string;
  children?: MarkdownNode[];
  data?: { hChildren?: MarkdownNode[] };
};

type Shortcode = { name: 'overrule' | 'wpex'; closing: boolean; more?: string };
type EditorialCorrection = { wp_id: number; location: string; original: string; replacement: string; reason: string; verification_status: string };

const assets = assetMap as Record<string, string>;
const publishedPaths = new Set(
  sourceIndex.filter((entry) => entry.status === 'publish').map((entry) => entry.legacy_path),
);
const legacyHostnames = new Set(['mathrao.com', 'www.mathrao.com']);

function applyEditorialCorrections(value: string, corrections: EditorialCorrection[], counts: Map<EditorialCorrection, number>): string {
  for (const correction of corrections) {
    const occurrences = value.split(correction.original).length - 1;
    if (occurrences) {
      counts.set(correction, (counts.get(correction) || 0) + occurrences);
      value = value.replaceAll(correction.original, correction.replacement);
    }
  }
  return value;
}

function decodedPath(pathname: string): string {
  try {
    return decodeURIComponent(pathname).normalize('NFC');
  } catch {
    return pathname;
  }
}

export function localLegacyUrl(value: string): string {
  if (!/^(?:https?:)?\/\//i.test(value)) return value;
  let url: URL;
  try {
    url = new URL(value.startsWith('//') ? `https:${value}` : value);
  } catch {
    return value;
  }
  if (!legacyHostnames.has(url.hostname.toLowerCase())) return value;
  const path = decodedPath(url.pathname);
  const asset = assets[path];
  if (asset) return `${encodeURI(asset)}${url.search}${url.hash}`;
  const canonical = publishedPaths.has(path) ? path : `${path.replace(/\/$/, '')}/`;
  if (publishedPaths.has(canonical)) return `${encodeURI(canonical)}${url.search}${url.hash}`;
  const alias = (slugAliases as Record<string, string>)[canonical];
  if (alias) return `${encodeURI(alias)}${url.search}${url.hash}`;
  return value;
}

function transformHtml(value: string): string {
  const compatibleMath = value.replace(/\$([^$]*?\\begin\{eqnarray\}[\s\S]*?\\end\{eqnarray\}[^$]*?)\$/g,
    (_whole, formula: string) => `$${compatibleEqnarray(formula)}$`);
  // One rescued formula (WP 714) used a bare MathJax environment in HTML.
  // Give its display-only conversion delimiters so the existing auto-render sees it.
  const delimitedMath = compatibleMath.replace(/\\begin\{eqnarray\}[\s\S]*?\\end\{eqnarray\}/g,
    (formula) => `$$${compatibleEqnarray(formula)}$$`);
  const withoutEmbeds = delimitedMath.replace(
    /<(?:iframe|object|embed|script|form)\b[^>]*>(?:[\s\S]*?<\/(?:iframe|object|embed|script|form)\s*>)?/gi,
    '<span class="legacy-embed-review" data-legacy-embed-review="true">[旧埋め込み：要確認]</span>',
  );
  const attributes = withoutEmbeds.replace(
    /\b(src|href|poster)\s*=\s*(["'])(.*?)\2/gi,
    (whole, name: string, quote: string, url: string) => {
      const local = localLegacyUrl(url.replace(/&amp;/g, '&'));
      return local === url ? whole : `${name}=${quote}${local.replace(/&/g, '&amp;')}${quote}`;
    },
  );
  return attributes.replace(
    /(?:https?:)?\/\/(?:www\.)?mathrao\.com\/[^\s"'<>]*/gi,
    (url) => localLegacyUrl(url),
  );
}

function compatibleEqnarray(value: string): string {
  const start = '\\begin{eqnarray}';
  const end = '\\end{eqnarray}';
  if (value.split(start).length !== 2 || value.split(end).length !== 2) return value;
  // eqnarray uses right/center/left columns around & = &. Preserve all cells.
  if (/&(?:amp;)?\s*=\s*&(?:amp;)?/.test(value)) {
    return value.replace(start, '\\begin{array}{rcl}').replace(end, '\\end{array}');
  }
  // The other legacy instances only use eqnarray as a wrapper around array.
  if (/\\left\s*\\\{[\s\S]*?\\begin\{array\}/.test(value)) {
    return value.replace(start, '').replace(end, '');
  }
  return value;
}

function escapeHtml(value: string): string {
  return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function extractShortcodes(node: MarkdownNode): Shortcode[] {
  const found: Shortcode[] = [];
  if ((node.type === 'text' || node.type === 'html') && node.value) {
    node.value = node.value.replace(/\[(\/)?(overrule|wpex)(?:\s+[^\]]*)?\]/gi, (token, slash: string | undefined, name: string) => {
      const more = token.match(/\bmore\s*=\s*["'“”‘’]([^"'“”‘’]+)["'“”‘’]/i)?.[1];
      found.push({ name: name.toLowerCase() as Shortcode['name'], closing: Boolean(slash), more });
      return '';
    });
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
    // A marker-only paragraph need not produce an empty paragraph.
    const empty = child.type === 'paragraph' && child.children?.every((item) => item.type === 'text' && !(item.value || '').trim());
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

/** Render-only transformation. The rescued Markdown remains byte-for-byte intact. */
export function remarkLegacyMarkdown() {
  return (tree: MarkdownNode, file: { path?: string }) => {
    const sourceName = file.path?.replace(/\\/g, '/').split('/').at(-1) || '';
    const wpId = Number(sourceName.match(/^wp-(\d{6})-/)?.[1]);
    const corrections = (errata as EditorialCorrection[]).filter((entry) => entry.wp_id === wpId);
    const counts = new Map<EditorialCorrection, number>();
    const visit = (node: MarkdownNode): void => {
      if ((node.type === 'math' || node.type === 'inlineMath') && node.value) {
        node.value = applyEditorialCorrections(node.value, corrections, counts);
        // HTML entities in the rescued HTML represent the original symbols.
        // Decode only for KaTeX input; the manuscript file is never changed.
        node.value = node.value
          .replace(/&gt;/gi, '>')
          .replace(/&lt;/gi, '<')
          .replace(/&amp;/gi, '&');
        node.value = compatibleEqnarray(node.value);
        // remark-math also stores the original text in hChildren at parse time.
        // rehype-katex reads that copy, so update both representations.
        const mathText = node.type === 'math'
          ? node.data?.hChildren?.[0]?.children?.[0]
          : node.data?.hChildren?.[0];
        if (mathText?.type === 'text') mathText.value = node.value;
      }
      if ((node.type === 'image' || node.type === 'link' || node.type === 'definition') && node.url) {
        node.url = localLegacyUrl(node.url);
      }
      if (node.type === 'html' && node.value) node.value = transformHtml(applyEditorialCorrections(node.value, corrections, counts));
      node.children?.forEach(visit);
    };
    visit(tree);
    for (const correction of corrections) {
      if (counts.get(correction) !== 1) {
        throw new Error(`Editorial correction for WP ${wpId} at ${correction.location} matched ${counts.get(correction) || 0} times (expected 1)`);
      }
    }
    renderShortcodes(tree);
  };
}
