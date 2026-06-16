## 2026-06-16 - Singleton Promise Caching for Static Assets
**Learning:** In static-site applications where data is loaded from CSV/JSON via fetch, redundant network requests and re-parsing during user interactions (like search or filtering) can significantly degrade performance and increase bandwidth usage.
**Action:** Implement a singleton promise pattern (e.g., `getPrompts()`) to cache the result of the fetch and parse operation. This ensures the expensive operation only happens once per session, even when triggered by frequent events like 'input' or 'change'.
