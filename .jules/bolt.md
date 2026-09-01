## 2025-05-10 - Singleton Promise Caching and Debouncing in Vanilla JS

**Learning:** Repeatedly fetching and parsing `/prompts.csv` on search input and audience toggle events in `script.js` caused unnecessary network traffic and main-thread parsing lag. In vanilla JS applications without state management frameworks, storing a singleton promise (`getPrompts()`) guarantees that `fetch` and `parseCSV` are executed exactly once per page lifecycle, while copying arrays prior to sorting (`[...rawPrompts].sort()`) prevents unintended cache mutations across consumers. Adding a 150ms debounce function prevents main-thread thrashing during fast typing.

**Action:** Always implement a singleton promise cache pattern with error resets when fetching static dataset CSVs/JSONs in vanilla JS components. Always operate on defensive array shallow copies (`[...data]`) when performing in-place operations like `.sort()` on cached state.
