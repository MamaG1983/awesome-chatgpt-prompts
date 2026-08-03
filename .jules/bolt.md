## 2026-08-03 - Singleton Promise Caching for Static CSV Prompts

**Learning:** Repeated fetching and parsing of static data resources (such as `prompts.csv` and `vibeprompts.csv`) on every interactive user action—like real-time filtering, search keystrokes, and audience mode toggles—creates severe main-thread blockages and redundant network latency. Implementing a singleton promise caching pattern completely avoids these overheads, resolving subsequent requests instantly.

**Action:** Wrap CSV fetch and parse operations in a cached singleton promise function (e.g., `getPrompts()` in `script.js` and `loadPrompts()` in `vibe/script.js`). Always clone the cached arrays before sorting or mutating them (e.g., `[...cachedPrompts].sort()`) to prevent side effects on other parts of the application sharing the cache.
