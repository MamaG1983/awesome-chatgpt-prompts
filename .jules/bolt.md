## 2026-08-31 - Singleton Promise Caching and Debouncing for Dynamic Search in Vibe Prompts

**Learning:** Repeated fetching and parsing of static CSV assets (`vibeprompts.csv`) on every user keystroke causes unnecessary network traffic and main-thread CPU spikes. Using a singleton promise cache (`promptsPromise`) eliminates redundant HTTP calls and parsing overhead, while a 150ms debounce function prevents main-thread thrashing during fast typing.
**Action:** Always wrap CSV/JSON fetch utilities in a singleton promise pattern that resets on error, and apply debouncing to rapid `input` event handlers for search/filter UI components.
