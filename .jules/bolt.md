## 2025-05-18 - Singleton Promise Caching for Static CSV Prompts

**Learning:** Repeatedly fetching and parsing `prompts.csv` (~113KB) and `vibeprompts.csv` (~29KB) on user interactions (such as keystrokes in search or toggling audience mode) causes unnecessary network overhead and main-thread CSV parsing lag. Using a singleton promise pattern allows concurrent and subsequent requests to await the same cached fetch/parse result while safely handling failures by resetting the promise on error to allow retries. When caching data that undergoes sorting (e.g. `initializeSearch`), always clone the cached array (`[...data].sort(...)`) to prevent mutating shared state.

**Action:** Wrap CSV loading logic in `getPrompts()`/`loadPrompts()` with a singleton promise cache and clone returned arrays before in-place mutations.
