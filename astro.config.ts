import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';
import { remarkLegacyMarkdown } from './src/lib/legacyMarkdown';

export default defineConfig({
  output: 'static',
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath, remarkLegacyMarkdown],
      rehypePlugins: [rehypeKatex],
    }),
  },
});
