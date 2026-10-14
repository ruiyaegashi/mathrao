// Temporary, manual Rakuten Books API smoke test. Do not log credentials or raw responses.
const appId = process.env.RAKUTEN_APP_ID;
const accessKey = process.env.RAKUTEN_ACCESS_KEY;
if (![appId, accessKey].every(Boolean)) {
  console.error('Required GitHub Actions secrets are missing.');
  process.exit(1);
}
// Temporary verification: compare two GitHub Secrets without printing either value.
// The confirmation secret must be freshly copied from the official Rakuten dashboard.
import { timingSafeEqual } from 'node:crypto';
const confirmedKey = process.env.RAKUTEN_ACCESS_KEY_CONFIRM;
if (!confirmedKey) {
  console.error('Confirmation Secret is missing. No API request was made.');
  process.exit(1);
}
const actualBuffer = Buffer.from(accessKey, 'utf8');
const confirmBuffer = Buffer.from(confirmedKey, 'utf8');
const matched = actualBuffer.length === confirmBuffer.length && timingSafeEqual(actualBuffer, confirmBuffer);
console.log(JSON.stringify({ check: 'rakuten-access-key-match', matched }));
process.exit(matched ? 0 : 1);

const searches = [{ title: '数学' }]; // known-good search on the official API test form
const results = [];
for (const search of searches) {
  const url = new URL('https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404');
  url.search = new URLSearchParams({
    applicationId: appId, ...search, format: 'json',
  }).toString();
  let status = 'error', title = '', image = false, itemLink = false, affiliateLink = false;
  let errorCode = 'none', errorMessageCategory = 'none';
  try {
    // Send the access key in a header, never a URL or logs.
    const response = await fetch(url, { headers: { accessKey }, redirect: 'error' });
    status = String(response.status);
    if (!response.ok) {
      // Extract only recognized, non-sensitive error categories. Never log raw responses.
      try {
        const error = await response.json();
        const rawCode = String(error.error ?? error.code ?? '').toLowerCase();
        const rawMessage = String(error.error_description ?? error.message ?? '').toLowerCase();
        const categories = ['invalid_application_id', 'invalid_access_key', 'invalid_parameter', 'forbidden', 'rate_limit', 'not_found', 'unauthorized'];
        errorCode = categories.find(c => rawCode.includes(c) || rawMessage.includes(c.replaceAll('_', ' '))) ?? 'unclassified';
        errorMessageCategory = /access.?key/.test(rawMessage) ? 'access-key' : /application.?id/.test(rawMessage) ? 'application-id' : /permission|scope/.test(rawMessage) ? 'permission' : /domain|origin|referer/.test(rawMessage) ? 'origin' : /limit|quota/.test(rawMessage) ? 'limit' : 'other';
      } catch { errorCode = 'unreadable'; }
    }
    if (response.ok) {
      const payload = await response.json();
      const item = payload.Items?.[0]?.Item ?? payload.Items?.[0] ?? payload.items?.[0]?.Item ?? payload.items?.[0]?.item;
      if (item) {
        title = String(item.title ?? item.itemName ?? '').slice(0, 120);
        image = Boolean(item.largeImageUrl || item.mediumImageUrl || item.smallImageUrl);
        itemLink = /^https:\/\//.test(item.itemUrl ?? '');
        affiliateLink = /^https:\/\//.test(item.affiliateUrl ?? '');
      }
    }
  } catch {
    status = 'network-error';
  }
  results.push({ search: 'title:数学', status, errorCode, errorMessageCategory, found: Boolean(title), title, image, itemLink, affiliateLink });
  // Respect the registered 1 request/second budget.
  await new Promise(resolve => setTimeout(resolve, 1200));
}
console.log(JSON.stringify({ tested: results.length, results }, null, 2));
if (results.some(x => x.status !== '200')) process.exitCode = 1;
