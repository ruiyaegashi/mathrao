import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const lessons = defineCollection({
  loader: glob({ base: './src/content/lessons', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
  }),
});

const legacy = defineCollection({
  loader: glob({ base: './src/content/legacy', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    wp_id: z.number(),
    content_type: z.enum(['post', 'page']),
    status: z.enum(['publish', 'draft']),
    published_at: z.string().nullable(),
    wp_date: z.string(),
    modified_at: z.string(),
    legacy_url: z.string().nullable(),
    legacy_path: z.string().nullable(),
    legacy_slug: z.string().nullable(),
    former_slugs: z.array(z.string()),
    parent_wp_id: z.number().nullable(),
    parent_title: z.string().nullable(),
    hierarchy: z.array(z.string()),
    category: z.array(z.string()),
    tags: z.array(z.string()),
    mathrao_section: z.string(),
    mathrao_grade: z.string().nullable(),
    mathrao_course: z.string().nullable(),
    source_content_sha256: z.string(),
  }),
});

export const collections = { lessons, legacy };
