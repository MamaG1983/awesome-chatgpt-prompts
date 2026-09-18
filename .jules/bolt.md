## 2026-09-18 - CSV Data Singleton Caching and Card Attribute Filtering in script.js
**Learning:** `filterPrompts()` in `script.js` was triggering a network request and CSV re-parse for `prompts.csv` on every search input or audience select toggle, followed by $O(N \cdot M)$ string comparison loops over DOM cards.
**Action:** Implement a singleton promise getter `getPrompts()` for caching parsed CSV results and attach a `data-for-devs` dataset attribute on prompt cards during initialization to allow $O(N)$ visibility toggling without DOM text matching.
