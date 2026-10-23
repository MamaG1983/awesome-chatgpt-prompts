## 2026-10-23 - Caching and Debouncing Vibe Prompts CSV Load & Search
**Learning:** In the `/vibe` subpage, `loadPrompts()` was previously fetching and parsing `vibeprompts.csv` on every `setupSearch()` input event, generating redundant network requests and synchronous CPU overhead during rapid typing.
**Action:** Use a singleton promise pattern (`cachedPromptsPromise`) in `loadPrompts()` to fetch and parse CSV data exactly once per session, combined with a 150ms `debounce` wrapper on the search input event listener to avoid main-thread thrashing.
