// Existing manual refresh can later be reused on Forgejo.
// API data must not be committed. Never log credentials, URLs, or API payloads.
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { join } from 'node:path';

const cwd = process.cwd();
const selectionPath = join(cwd, 'src/data/rakuten-book-selections.json');
const outputPath = join(cwd, 'src/generated/rakuten-books.json');
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const { schemaVersion, selections } = JSON.parse(await readFile(selectionPath, 'utf8'));
if (schemaVersion !== 2 || !Array.isArray(selections) || !selections.length) {
  throw new Error('Invalid selection list.');
}
const slots = new Set();
const isbns = [];
for (const selected of selections) {
  const { articlePath, legacySlotIndex, isbns: books } = selected;
  if (!/^\/[a-z0-9-]+\/$/.test(articlePath) || !Number.isInteger(legacySlotIndex) ||
      legacySlotIndex < 1 || !Array.isArray(books) || !books.length) {
    throw new Error('Invalid selected article, position or books.');
  }
  const key = articlePath + legacySlotIndex;
  if (slots.has(key)) throw new Error('Duplicate selected position.');
  slots.add(key);
  if (books.some(isbn => typeof isbn !== 'string' || !/^[0-9]{13}$/.test(isbn))) {
    throw new Error('Invalid ISBN.');
  }
  isbns.push(...books);
}
if (new Set(isbns).size !== isbns.length) throw new Error('Duplicate selected ISBN.');
if (process.argv.includes('--check-selections')) {
  console.log(JSON.stringify({ groups: selections.length, books: isbns.length }));
  process.exit(0);
}
const { RAKUTEN_APP_ID: appId, RAKUTEN_ACCESS_KEY: accessKey, RAKUTEN_AFFILIATE_ID: affiliateId } = process.env;
if (![appId, accessKey, affiliateId].every(Boolean)) throw new Error('Missing required GitHub Actions secrets.');
const output = {};
const noExactMatch = [];
const incompleteMetadata = [];
for (let i = 0; i < isbns.length; i++) {
  if (i) await sleep(1200);
  const isbn = isbns[i];
  const url = new URL('https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404');
  url.search = new URLSearchParams({ applicationId: appId, affiliateId, isbn, format: 'json' }).toString();
  const response = await fetch(url, { headers: { accessKey }, redirect: 'error' });
  if (!response.ok) throw new Error('Rakuten Books API HTTP ' + response.status + ' for ISBN ' + isbn);
  const data = await response.json();
  const matched = (data.Items ?? []).map(x => x.Item ?? x).find(x => String(x.isbn ?? '') === isbn);
  if (!matched) { noExactMatch.push(isbn); continue; }
  const title = String(matched.title ?? '');
  const imageUrl = String(matched.largeImageUrl || matched.mediumImageUrl || matched.smallImageUrl || '');
  const affiliateUrl = String(matched.affiliateUrl ?? '');
  const validHttps = value => { try { return new URL(value).protocol === 'https:'; } catch { return false; } };
  if (!title || !validHttps(imageUrl) || !validHttps(affiliateUrl)) { incompleteMetadata.push(isbn); continue; }
  const record = { isbn, title, imageUrl, affiliateUrl, fetchedAt: new Date().toISOString() };
  output[isbn] = record;
}
// Log only ISBN identifiers and verification status; never log product payloads or URLs.
console.log(JSON.stringify({
  checked: isbns.length,
  exactMatches: Object.keys(output).length,
  noExactMatch,
  incompleteMetadata,
}));
if (noExactMatch.length || incompleteMetadata.length) {
  throw new Error('Rakuten ISBN verification failed: ' + (noExactMatch.length + incompleteMetadata.length) + ' item(s)');
}
if (process.argv.includes('--audit')) {
  console.log('ISBN audit: PASS (no file written and no deployment)');
  process.exit(0);
}
await mkdir(join(cwd, 'src/generated'), { recursive: true });
await writeFile(outputPath, JSON.stringify({ schemaVersion: 2, books: output }, null, 2) + '\n', { mode: 0o600 });
console.log(JSON.stringify({ approvedGroups: selections.length, matchedBooks: isbns.length, temporaryData: true }));
