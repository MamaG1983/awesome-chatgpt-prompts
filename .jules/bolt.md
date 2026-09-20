## 2026-09-20 - Cache CSV Fetching and Eliminate O(N²) DOM Matching on Audience Toggle

**Learning:** `filterPrompts()` was issuing an HTTP fetch request and re-parsing `prompts.csv` on every audience selection change or search filter action. Furthermore, `filterPrompts()` iterated over all rendered prompt card DOM elements and performed $O(N \times M)$ regex string matching against CSV prompt titles to check `for_devs` status.
**Action:** Use a singleton promise cache for `prompts.csv` fetching/parsing via `getPrompts()`, and tag generated card elements with a `data-for-devs="true"` attribute in `createPromptCards()` for $O(1)$ dataset checks when toggling card visibility.
