## 2026-10-13 - Singleton Promise Caching for Static CSV Files

**Learning:** `script.js` was triggering multiple redundant fetches and parsing of `prompts.csv` (~115KB) across `initializeSearch`, `filterPrompts`, and `createPromptCards`. Storing the fetch/parse sequence as a singleton Promise (`getPrompts()`) caches the parsed array across the entire page lifecycle. Mutating operations like `.sort()` must operate on a cloned array (`[...rawPrompts].sort(...)`) to avoid corrupting the shared cached data. Resetting the promise on `.catch()` ensures network retries remain possible on temporary failures.

**Action:** Wrap repeated static asset fetches in a singleton promise caching function, and always clone arrays before in-place mutations like `.sort()`.
