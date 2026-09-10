## 2025-05-10 - Singleton Promise Caching and Debouncing for Vibe Prompts

**Learning:** On the `/vibe` route, `loadPrompts()` was previously making fresh HTTP requests and re-parsing `vibeprompts.csv` on every `input` search event. Caching the `fetch` and `parseCSV` result via a singleton promise pattern eliminates redundant network requests and CPU overhead. Adding a 150ms debounce to the search `input` event prevents rapid DOM re-rendering thrashing during typing.

**Action:** Always wrap CSV/JSON fetching functions in a singleton promise cache when the data is static per session, and debounce user input listeners on search fields.
