# Bolt's Performance Journal

## Critical Learnings

## 2026-11-07 - Singleton Promise Caching for Static CSV Assets in Vibe Page
**Learning:** In static Jekyll SPAs with client-side CSV processing, functions fetching CSV datasets can be called across multiple independent render/search cycles. In `vibe/script.js`, `loadPrompts()` was called twice during initial render (`renderMainPrompts()` and `renderSidebarPrompts()`), and on every single keystroke in `#searchInput`, repeatedly re-fetching `/vibeprompts.csv` over the network and re-parsing CSV text with regex matching.
**Action:** Use a singleton promise cache (`promptsCachePromise`) that caches both the network fetch and the parsed CSV array across all callers, while resetting to `null` on fetch failure to allow retries.
