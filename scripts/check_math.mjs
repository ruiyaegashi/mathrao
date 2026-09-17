/** Locate KaTeX failures in rescued Markdown without changing the manuscript. */
import { readFileSync, readdirSync, mkdirSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { createMarkdownProcessor } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import katex from 'katex';

const root = resolve(import.meta.dirname, '..');
const files = readdirSync(join(root, 'src/content/legacy')).filter((name) => name.endsWith('.md'));
const selectedId = process.argv.includes('--id') ? Number(process.argv[process.argv.indexOf('--id') + 1]) : null;
let collected = [];

function collectMath() {
  return (tree) => {
    const walk = (node) => {
      if (node.type === 'math' || node.type === 'inlineMath') {
        collected.push({ expression: node.value, line: node.position?.start?.line ?? null, source: node.type });
      }
      if (node.type === 'html' && node.value) {
        const startingLine = node.position?.start?.line ?? 1;
        const regex = /(?<!\\)(?<!\$)\$(?!\$)([\s\S]*?)(?<!\\)\$(?!\$)/g;
        for (const match of node.value.matchAll(regex)) {
          collected.push({
            expression: match[1],
            line: startingLine + node.value.slice(0, match.index).split('\n').length - 1,
            source: 'raw_html',
          });
        }
      }
      node.children?.forEach(walk);
    };
    walk(tree);
  };
}

const processor = await createMarkdownProcessor({
  remarkPlugins: [remarkMath, collectMath],
  rehypePlugins: [],
  syntaxHighlight: false,
});

const results = [];
for (const name of files) {
  const full = readFileSync(join(root, 'src/content/legacy', name), 'utf8');
  const end = full.indexOf('\n---', 4);
  if (end < 0) throw new Error(`Missing front matter end: ${name}`);
  const front = full.slice(4, end).split(/\r?\n/);
  const field = (key) => JSON.parse(front.find((line) => line.startsWith(`${key}: `)).slice(key.length + 2));
  const wpId = field('wp_id');
  if (selectedId && wpId !== selectedId) continue;
  const title = field('title');
  const body = full.slice(end + 4);
  const frontLines = full.slice(0, end + 4).split('\n').length - 1;
  collected = [];
  await processor.render(body);
  const errors = [];
  const warnings = [];
  for (const item of collected) {
    const strictWarnings = [];
    const expression = item.expression.replace(/&gt;/gi, '>').replace(/&lt;/gi, '<').replace(/&amp;/gi, '&');
    try {
      katex.renderToString(expression, {
        throwOnError: true,
        strict: (code, message) => { strictWarnings.push({ code, message }); return 'ignore'; },
      });
    } catch (error) {
      errors.push({ line: (item.line ?? 1) + frontLines, source: item.source, expression: item.expression, error: String(error.message ?? error) });
    }
    for (const warning of strictWarnings) {
      warnings.push({ line: (item.line ?? 1) + frontLines, source: item.source, expression: item.expression, ...warning });
    }
  }
  results.push({ wp_id: wpId, title, file: name, expressions: collected.length, errors, warnings });
}

const summary = {
  pages_checked: results.length,
  pages_with_math: results.filter((item) => item.expressions).length,
  expressions: results.reduce((n, item) => n + item.expressions, 0),
  pages_with_errors: results.filter((item) => item.errors.length).length,
  errors: results.reduce((n, item) => n + item.errors.length, 0),
  pages_with_warnings: results.filter((item) => item.warnings.length).length,
  warnings: results.reduce((n, item) => n + item.warnings.length, 0),
  wp1125_expressions: results.find((item) => item.wp_id === 1125)?.expressions ?? null,
};
const report = { summary, pages: results.filter((item) => item.errors.length || item.warnings.length) };
if (!selectedId) {
  mkdirSync(join(root, 'reports'), { recursive: true });
  writeFileSync(join(root, 'reports/math-validation.json'), JSON.stringify(report, null, 2) + '\n');
}
console.log(JSON.stringify(selectedId ? { summary, page: results[0] } : summary, null, 2));
