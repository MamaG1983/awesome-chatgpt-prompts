## 2026-09-14 - Promise Singleton & Dataset Attributes for Card Visibility

**Learning:** Re-fetching `/prompts.csv` and running O(N^2) DOM title matching on every audience selector change caused redundant network requests and CPU overhead. Caching the parsed CSV promise and tagging prompt card DOM elements with `data-for-devs="true|false"` during card generation enables O(1) visibility toggling per card and eliminates redundant fetches.

**Action:** Always store metadata on DOM dataset attributes during initial rendering when cards/items need dynamic filtering, and cache network resources using singleton promises.
