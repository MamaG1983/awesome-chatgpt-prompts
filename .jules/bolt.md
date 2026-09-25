## 2025-05-18 - Singleton CSV Fetch Promise & O(N) DOM Card Filtering

**Learning:** `filterPrompts()` in `script.js` was triggering a fresh `fetch("/prompts.csv")` network request and CSV parse on every audience toggle or search filter. Additionally, for each card in the DOM, it was running `prompts.find()` with string normalization and substring checks across the entire CSV dataset, resulting in O(N * M) performance overhead on every filter operation.
**Action:** Use a singleton promise cache (`getPrompts()`) for fetching and parsing CSVs. Attach `data-for-devs` attributes directly onto prompt card DOM elements during card creation so audience toggles can run in O(N) without array lookups or regex/string parsing.
