## 2026-08-29 - Singleton Promise Caching and Dataset Attributes for Prompts Filtering

**Learning:** Re-fetching and re-parsing `prompts.csv` on every audience switch or filtering trigger causes unnecessary network requests and O(N*M) DOM-to-CSV title string matching. Using a singleton promise `getPrompts()` caches the fetch/parse result once, and setting `data-for-devs` attributes directly on prompt card elements during DOM construction enables instant O(N) visibility toggling.

**Action:** Whenever a static asset (like CSV/JSON data) is needed by multiple interactive UI functions, wrap its retrieval in a singleton promise cache and store metadata directly as `data-*` attributes on target DOM elements during creation.
