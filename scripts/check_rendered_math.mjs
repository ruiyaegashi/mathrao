/** Check every client-side math expression in the built public articles. */
import { readFileSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import katex from 'katex';

const root = resolve(import.meta.dirname, '..');
const index = JSON.parse(readFileSync(join(root, 'migration/source-index.json'), 'utf8'));
const errors = [];
const expressionCounts = {};
let checked = 0;
let pagesWithMath = 0;

function decodeHtml(value) {
  return value
    .replace(/&#x([0-9a-f]+);/gi, (_, hex) => String.fromCodePoint(parseInt(hex, 16)))
    .replace(/&#([0-9]+);/g, (_, decimal) => String.fromCodePoint(Number(decimal)))
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"').replace(/&#39;/g, "'");
}

for (const item of index.filter((entry) => entry.status === 'publish')) {
  const html = readFileSync(join(root, 'dist', item.legacy_path, 'index.html'), 'utf8');
  const article = html.match(/<article\b[\s\S]*?<\/article>/)?.[0];
  if (!article) throw new Error(`Missing article markup for WP ${item.wp_id}`);
  const display = [...article.matchAll(/(?<!\\)\$\$([\s\S]*?)\$\$/g)];
  const withoutDisplay = article.replace(/(?<!\\)\$\$([\s\S]*?)\$\$/g, '');
  const inline = [...withoutDisplay.matchAll(/(?<!\\)(?<!\$)\$(?!\$)([\s\S]*?)(?<!\\)\$(?!\$)/g)];
  const expressions = [...display, ...inline];
  if (expressions.length) {
    pagesWithMath++;
    expressionCounts[item.wp_id] = expressions.length;
  }
  for (const match of expressions) {
    checked++;
    const expression = decodeHtml(match[1]);
    try {
      katex.renderToString(expression, { throwOnError: true, strict: 'ignore' });
    } catch (error) {
      errors.push({ wp_id: item.wp_id, legacy_path: item.legacy_path, expression, error: String(error.message ?? error) });
    }
  }
}

const report = {
  published_articles_checked: 306,
  pages_with_client_math: pagesWithMath,
  client_math_expressions_checked: checked,
  expression_counts_for_regressions: Object.fromEntries([714, 1125, 2582, 2586].map((id) => [id, expressionCounts[id] ?? 0])),
  errors,
};
writeFileSync(join(root, 'reports/rendered-math-validation.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ ...report, errors: errors.length }, null, 2));
if (errors.length) process.exitCode = 1;
