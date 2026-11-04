## 2026-11-04 - Singleton Promise Caching for Static CSV Datasets
**Learning:** In client-side search implementations on static Jekyll sites, un-memoized data loading functions invoked on event handlers (such as `input` on search boxes) trigger redundant network round-trips and repeated CPU-bound regex CSV parsing on every keystroke.
**Action:** Use a singleton promise pattern (`promptsCachePromise`) that caches both the in-flight fetch and the parsed result across function calls, resetting to `null` on failure so error recovery is preserved without penalizing normal interactions.
