## 2026-10-12 - Singleton Promise Caching for Static CSV Fetches
**Learning:** Repeatedly fetching and re-parsing static CSV dataset files (`prompts.csv` and `vibeprompts.csv`) on UI interactions (such as audience toggling, component rendering, or search calls) creates unnecessary network requests and main-thread parsing overhead.
**Action:** Wrap fetch and CSV parsing calls in a module-level singleton promise (`promptsPromise`) that caches the parsed result and resets to `null` on failure for safe retries.
