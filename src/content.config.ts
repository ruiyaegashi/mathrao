import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const articles = defineCollection({
  loader: glob({ base: './src/content/legacy', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    status: z.enum(['publish', 'draft']).default('publish'),
    published_at: z.string().nullable().optional(),
    path: z.string().optional(),
    legacy_path: z.string().nullable().optional(),
    wp_id: z.number().optional(),
  }).refine((data) => data.status === 'draft' || Boolean(data.path ?? data.legacy_path), {
    message: 'published article requires path or legacy_path',
  }),
});

export const collections = { articles };
