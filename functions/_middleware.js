function objectHeaders(object) {
  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set('etag', object.httpEtag);
  headers.set('last-modified', object.uploaded.toUTCString());
  headers.set('cache-control', 'public, max-age=3600');
  return headers;
}

function decodePathname(url) {
  try {
    return decodeURIComponent(url.pathname);
  } catch {
    return null;
  }
}

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const pathname = decodePathname(url);

  if (pathname === null || !pathname.startsWith('/media/')) return context.next();

  if (request.method !== 'GET' && request.method !== 'HEAD') {
    return new Response(null, {
      status: 405,
      headers: { Allow: 'GET, HEAD' },
    });
  }

  const key = pathname.slice('/media/'.length);
  if (!key || key.includes('/')) return new Response(null, { status: 404 });

  if (request.method === 'HEAD') {
    const object = await env.MEDIA.head(key);
    if (!object) return new Response(null, { status: 404 });
    const headers = objectHeaders(object);
    headers.set('content-length', String(object.size));
    return new Response(null, { headers });
  }

  const object = await env.MEDIA.get(key);
  if (!object) return new Response(null, { status: 404 });

  const headers = objectHeaders(object);
  headers.set('content-length', String(object.size));
  return new Response(object.body, { headers });
}
