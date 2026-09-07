# Bolt's Journal

## 2026-09-07 - Singleton Promise Caching for CSV Data Fetching

**Learning:** Re-fetching and re-parsing static CSV prompt files on initial load and on every search/filter operation causes unnecessary network overhead and main-thread CPU blocking. Wrapping the CSV fetch and parse operation in a singleton promise ensures the CSV is requested and parsed exactly once per session while allowing multiple asynchronous callers to await the same cached data safely.

**Action:** When working with client-side static dataset files (e.g., CSVs or JSONs) that are accessed across multiple event handlers or components, always use a singleton promise pattern (`promptsPromise`) with error-reset logic rather than issuing repeated `fetch` calls.
