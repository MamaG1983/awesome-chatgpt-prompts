## 2026-08-24 - Singleton Promise Caching for Static CSV Assets

**Learning:** In static Jekyll applications with client-side CSV processing, repeated `fetch()` calls on user events (such as dropdown filter toggles or search input keystrokes) cause unnecessary network re-fetches and redundant CSV regex parsing overhead on the main thread.

**Action:** Wrap CSV loading logic in an in-memory singleton promise (`getPrompts()`) that caches the initial `fetch()` + `parseCSV()` promise. On error, reset the promise to `null` to allow retries while ensuring all subsequent UI interactions reuse the cached result instantly.
