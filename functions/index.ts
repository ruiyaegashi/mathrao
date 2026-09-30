import sourceIndex from '../migration/source-index.json';

type SourceItem = {
  wp_id: number;
  status: string;
  legacy_path: string | null;
};

const publishedPaths = new Map(
  (sourceIndex as SourceItem[])
    .filter((item) => item.status === 'publish' && item.legacy_path)
    .map((item) => [String(item.wp_id), item.legacy_path as string]),
);

export const onRequestGet = async (context: {
  request: Request;
  next: () => Promise<Response>;
}) => {
  const url = new URL(context.request.url);
  const wpId = url.searchParams.get('p');

  if (wpId === null) {
    return context.next();
  }

  if (!/^\d+$/.test(wpId)) {
    return new Response('Not Found', { status: 404 });
  }

  const canonicalPath = publishedPaths.get(wpId);

  if (!canonicalPath) {
    return new Response('Not Found', { status: 404 });
  }

  return Response.redirect(
    new URL(canonicalPath, url.origin).toString(),
    301,
  );
};
