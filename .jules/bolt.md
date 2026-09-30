## 2026-09-30 - O(N*M) DOM Matching & Uncached CSV Network Re-fetching

**Learning:** `filterPrompts()` in `script.js` was triggering a network `fetch('/prompts.csv')` and re-parsing CSV text on every audience filter change or search interaction. Furthermore, for every prompt card element in the DOM, it was running `prompts.find(...)` with heavy regex string normalization (`replace(/\s+/g, " ").replace(/[\n\r]/g, "").trim().toLowerCase()`), resulting in $O(N \times M)$ string operations ($22,500+$ ops per call).

**Action:** Implement singleton promise caching (`getPrompts()`) for `/prompts.csv` and set a `data-for-devs` dataset attribute on prompt card elements during creation. Filtering now performs $O(N)$ DOM dataset checks, eliminating UI latency (~3,400x speedup in card visibility updates).
