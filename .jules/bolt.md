## 2025-05-20 - Singleton Promise Caching for CSV Data in Vibe Mode

**Learning:** In static Jekyll prompt applications fetching client-side CSV files (`/vibeprompts.csv`), calling un-cached `loadPrompts()` inside event listeners (e.g. `input` events during search) triggers redundant HTTP requests and CPU-heavy CSV string re-parsing on every keystroke.
**Action:** Store the initial fetch/parse promise in a singleton variable (`promptsPromise`) so all callers share the cached data promise while ensuring error recovery by setting `promptsPromise = null` on failure.
