## 2026-10-04 - Singleton Promise Caching & Input Debouncing on Vibe Prompts

**Learning:** On the `/vibe` page, `loadPrompts()` was previously called directly inside the search input event listener, causing `vibeprompts.csv` to be fetched and parsed on every single keystroke. Combining singleton promise caching (`loadPrompts()`) with a 150ms `debounce` wrapper eliminates redundant network calls and main-thread parsing completely during rapid typing.

**Action:** Always wrap data fetching for static CSV assets in singleton promises, and wrap high-frequency event listeners (like input typing) in debounce functions.
