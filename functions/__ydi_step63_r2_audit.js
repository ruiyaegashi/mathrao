export async function onRequestGet({ env }) {
  if (!env.MEDIA) {
    return new Response(JSON.stringify({ error: "MEDIA binding missing" }), {
      status: 500,
      headers: { "content-type": "application/json; charset=utf-8" },
    });
  }

  const objects = [];
  let cursor;
  do {
    const page = await env.MEDIA.list({ limit: 1000, cursor });
    for (const object of page.objects ?? []) {
      objects.push({ key: object.key, size: object.size });
    }
    cursor = page.truncated ? page.cursor : undefined;
  } while (cursor);

  objects.sort((a, b) => a.key.localeCompare(b.key));
  return new Response(JSON.stringify({
    bucket: "mathrao-media",
    count: objects.length,
    total_bytes: objects.reduce((sum, object) => sum + object.size, 0),
    objects,
  }), {
    status: 200,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}
