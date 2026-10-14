// Temporary, manual Rakuten Books API smoke test. Do not log credentials or raw responses.
const appId = process.env.RAKUTEN_APP_ID;
const accessKey = process.env.RAKUTEN_ACCESS_KEY;
const affiliateId = process.env.RAKUTEN_AFFILIATE_ID;
if (![appId, accessKey, affiliateId].every(Boolean)) {
  console.error('Required GitHub Actions secrets are missing.');
  process.exit(1);
}
// Five representative title queries for mathematics books; first hit per query.
const searches = [
  { title: 'チャート式 基礎からの 数学1＋A' },
  { title: 'チャート式 基礎からの 数学2＋B' },
  { title: 'チャート式 基礎からの 数学3＋C' },
  { title: '数学ガール' },
  { title: '数学 入門問題精講' },
];
const results = [];
for (const search of searches) {
  const url = new URL('https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404');
  url.search = new URLSearchParams({
    applicationId: appId, affiliateId, ...search, format: 'json',
  }).toString();
  let status = 'error', title = '', isbn = '', image = false, itemLink = false, affiliateLink = false;
  let errorCode = 'none', errorMessageCategory = 'none';
  try {
    // Send the access key in a header, never a URL or logs.
    const response = await fetch(url, { headers: { accessKey }, redirect: 'error' });
    status = String(response.status);
    if (!response.ok) {
      // Do not emit the error body, request URL, headers or any credentials.
      // Map only preapproved diagnostic tokens from up to 2 KiB of error body.
      const type = (response.headers.get('content-type') ?? '').toLowerCase();
      errorCode = type.includes('json') ? 'json-response' : type.includes('html') ? 'html-response' : 'other-response';
      try {
        const body = (await response.text()).slice(0, 2048).toLowerCase();
        const patterns = [
          ['client-ip-not-allowed', /client_ip_not_allowed|client.ip.not.allowed/],
          ['referer-not-allowed', /referer|referrer/],
          ['origin-not-allowed', /origin|allowed.website|domain/],
          ['not-authorized', /not_authorized|not authorized|permission|scope/],
          ['access-key-error', /invalid.access.key|access.key|accesskey/],
          ['app-id-error', /application.id|applicationid/],
          ['rate-limited', /rate.limit|quota|too.many.requests/],
          ['security-block', /access.denied|request.blocked|security.policy|forbidden/]
        ];
        errorMessageCategory = patterns.find(([, re]) => re.test(body))?.[0] ?? 'unknown';
      } catch {
        errorMessageCategory = 'unreadable';
      }
    }
    if (response.ok) {
      const payload = await response.json();
      const item = payload.Items?.[0]?.Item ?? payload.Items?.[0] ?? payload.items?.[0]?.Item ?? payload.items?.[0]?.item;
      if (item) {
        title = String(item.title ?? item.itemName ?? '').slice(0, 120);
        isbn = String(item.isbn ?? '').slice(0, 20);
        image = Boolean(item.largeImageUrl || item.mediumImageUrl || item.smallImageUrl);
        itemLink = /^https:\/\//.test(item.itemUrl ?? '');
        affiliateLink = /^https:\/\//.test(item.affiliateUrl ?? '');
      }
    }
  } catch {
    status = 'network-error';
  }
  results.push({ search: search.title, status, errorCode, errorMessageCategory, found: Boolean(title), title, isbn, image, itemLink, affiliateLink });
  // Respect the registered 1 request/second budget.
  await new Promise(resolve => setTimeout(resolve, 1200));
}
console.log(JSON.stringify({ tested: results.length, results }, null, 2));
const uniqueIsbns = new Set(results.map(x => x.isbn).filter(Boolean));
if (results.some(x => x.status !== '200' || !x.found || !x.image || !x.itemLink || !x.affiliateLink)) process.exitCode = 1;
if (uniqueIsbns.size !== results.length) {
  console.error('Five distinct ISBNs were not confirmed.');
  process.exitCode = 1;
}
