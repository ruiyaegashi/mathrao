import { getCollection, type CollectionEntry } from 'astro:content';

export const sections = [
  { slug: 'junior-high', title: '中学数学', grouping: 'grade' },
  { slug: 'high-school', title: '高校数学', grouping: 'course' },
  { slug: 'theorems', title: '定理・公式・証明', grouping: 'course' },
  { slug: 'instant', title: 'インスタント中高数学', grouping: 'none' },
  { slug: 'columns', title: 'コラム', grouping: 'none' },
  { slug: 'study-methods', title: '勉強法', grouping: 'none' },
  { slug: 'math-ability', title: '数学力', grouping: 'none' },
  { slug: 'cram-schools', title: '塾・予備校', grouping: 'none' },
  { slug: 'other', title: 'その他', grouping: 'none' },
] as const;

export type LegacyEntry = CollectionEntry<'legacy'>;
export type Section = (typeof sections)[number];

const gradeOrder = ['中1', '中2', '中3'];
const courseOrder = ['数学I', '数学A', '数学II', '数学B', '数学III'];

export async function getPublishedLegacy(): Promise<LegacyEntry[]> {
  const entries = await getCollection('legacy', ({ data }) => data.status === 'publish');
  const knownSections = new Set<string>(sections.map((section) => section.title));
  for (const entry of entries) {
    if (!entry.data.legacy_path || !knownSections.has(entry.data.mathrao_section)) {
      throw new Error(`Catalog entry needs a legacy path and known section: WP ${entry.data.wp_id}`);
    }
  }
  return entries.sort((a, b) => a.data.wp_id - b.data.wp_id);
}

export function entriesForSection(entries: LegacyEntry[], section: Section): LegacyEntry[] {
  return entries.filter((entry) => entry.data.mathrao_section === section.title);
}

export function groupsForSection(entries: LegacyEntry[], section: Section) {
  if (section.grouping === 'none') {
    return [{ label: '記事一覧', entries }];
  }

  const key = section.grouping === 'grade' ? 'mathrao_grade' : 'mathrao_course';
  const order = section.grouping === 'grade' ? gradeOrder : courseOrder;
  const groupNames = [...order, '案内・対応表'];
  return groupNames
    .map((label) => ({
      label,
      entries: entries.filter((entry) => {
        const value = entry.data[key];
        return (value && order.includes(value) ? value : '案内・対応表') === label;
      }),
    }))
    .filter((group) => group.entries.length > 0);
}
