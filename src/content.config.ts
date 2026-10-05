import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const articles = defineCollection({
  loader: glob({ base: './src/content/articles', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    status: z.enum(['published', 'draft']).default('published'),
    published_at: z.string().nullable().optional(),
    path: z.string().optional(),
    featured_image: z.string().optional(),
  }).refine((data) => data.status === 'draft' || Boolean(data.path), {
    message: 'published article requires path',
  }),
});

export const collections = { articles };
