import { rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

// Astro caches rendered content without tracking this project's render-only
// editorial data. Refresh it before each production build.
const root = dirname(dirname(fileURLToPath(import.meta.url)));
rmSync(join(root, 'node_modules', '.astro'), { recursive: true, force: true });
