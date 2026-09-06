## 2026-09-06 - Singleton Promise Caching & DOM Tagging for Card Visibility

**Learning:** Re-fetching `/prompts.csv` and re-parsing CSV text during audience filtering or search input caused redundant network requests and CPU overhead (~113KB CSV parsing per event). Furthermore, using nested O(N^2) loops with regex string replacements to match prompt titles between CSV entries and DOM cards on every toggle created avoidable main-thread lag.
**Action:** Use a singleton promise cache (`getPrompts()`) to parse CSV data once, tag cards with `data-for-devs="true"|"false"` during DOM element creation, and perform O(N) attribute checks for audience filtering.
