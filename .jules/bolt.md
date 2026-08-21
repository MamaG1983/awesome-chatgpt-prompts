## 2026-08-21 - Singleton Promise Caching for Vibe Coding CSV Prompts
**Learning:** In `vibe/script.js`, data loading for `/vibeprompts.csv` was previously executed inside `loadPrompts()` on every search keystroke in `setupSearch()`, causing redundant network requests and CSV parsing on each user input.
**Action:** Implement singleton promise caching in `loadPrompts()` so the CSV text is fetched and parsed at most once per page load, while resetting the promise on failure for retries.
