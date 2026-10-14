// Manual pilot only: create short-lived book data for one existing article.
// Never log credentials, request URLs or raw API responses, and never commit the output.
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { join } from 'node:path';

const cwd = process.cwd();
const selectionPath = join(cwd, 'src/data/rakuten-book-selections.json');
const outputPath = join(cwd, 'src/generated/rakuten-books.json');
const ttlMs = 7 * 24 * 60 * 60 * 1000;

function isFresh(record, now) {
  const from = Date.parse(record?.fetchedAt ?? '');
  const until = Date.parse(record?.expiresAt ?? '');
  return Number.isFinite(from) && Number.isFinite(until) &&
    from <= now && now < until && until - from <= ttlMs;
}

if (process.argv.includes('--check-expiry')) {
  const now = Date.now();
  const sample = { fetchedAt: new Date(now).toISOString(), expiresAt: new Date(now + ttlMs).toISOString() };
  if (!isFresh(sample, now) || isFresh(sample, now + ttlMs) || isFresh(sample, now - 1)) {
    throw new Error('Expiry boundary check failed.');
  }
  console.log('Expiry boundary check: PASS (fresh visible, expired hidden).');
  process.exit(0);
}

const { RAKUTEN_APP_ID: appId, RAKUTEN_ACCESS_KEY: accessKey, RAKUTEN_AFFILIATE_ID: affiliateId } = process.env;
if (![appId, accessKey, affiliateId].every(Boolean)) {
  throw new Error('Missing required GitHub Actions secrets.');
}

const selections = JSON.parse(await readFile(selectionPath, 'utf8')).selections;
if (!Array.isArray(selections) || selections.length !== 1) throw new Error('Pilot requires exactly one selection.');
const selected = selections[0];
const isbn = String(selected.isbn ?? '');
if (!/^[0-9]{13}$/.test(isbn)) throw new Error('Invalid selected ISBN.');

const url = new URL('https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404');
url.search = new URLSearchParams({ applicationId: appId, affiliateId, isbn, format: 'json' }).toString();
const response = await fetch(url, { headers: { accessKey }, redirect: 'error' });
if (!response.ok) throw new Error('Rakuten Books API returned HTTP ' + response.status);
const data = await response.json();
const items = (data.Items ?? []).map(x => x.Item ?? x);
const matched = items.find(item => String(item.isbn ?? '') === isbn);
if (!matched) throw new Error('No exact ISBN match was found. No output produced.');

const title = String(matched.title ?? '');
const imageUrl = String(matched.largeImageUrl || matched.mediumImageUrl || matched.smallImageUrl || '');
const affiliateUrl = String(matched.affiliateUrl ?? '');
if (!title || ![imageUrl, affiliateUrl].every(x => {
  try { return new URL(x).protocol === 'https:'; } catch { return false; }
})) throw new Error('Book title, HTTPS cover, or HTTPS affiliate URL missing.');
const now = Date.now();
const fetchedAt = new Date(now).toISOString();
const expiresAt = new Date(now + ttlMs).toISOString();
const record = { isbn, title, imageUrl, affiliateUrl, fetchedAt, expiresAt };
if (!isFresh(record, now)) throw new Error('New record failed freshness validation.');
const output = { schemaVersion: 1, books: { [isbn]: record } };
await mkdir(join(cwd, 'src/generated'), { recursive: true });
await writeFile(outputPath, JSON.stringify(output, null, 2) + '\n', { mode: 0o600 });
// Only approved non-sensitive fields are written to job logs.
console.log(JSON.stringify({ tested: 1, matchedIsbn: true, hasImage: true, hasAffiliateUrl: true, validDays: 7 }));
