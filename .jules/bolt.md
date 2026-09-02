## 2025-09-02 - Singleton Promise Caching and Input Debouncing in Vibe Subpage

**Learning:** The `/vibe` section in `vibe/script.js` was fetching and parsing `/vibeprompts.csv` (~29KB) repeatedly on initial page load (both `renderMainPrompts()` and `renderSidebarPrompts()`) and on every single keystroke in the search input without debouncing. This caused redundant network requests and CPU overhead on typing.
**Action:** Use a singleton `promptsPromise` cache pattern for `loadPrompts()` that resets to `null` on error, and wrap the search input listener with a 150ms `debounce()` function to eliminate redundant network fetches and main-thread parsing lag.
