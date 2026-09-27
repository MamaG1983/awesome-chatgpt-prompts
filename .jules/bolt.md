## 2026-09-27 - Singleton Promise Caching and Search Debouncing in Vibe Subpage
**Learning:** In static Jekyll client-side apps, components that trigger `loadPrompts()` on initialization and per input event (e.g. search input) cause network fetch spikes and redundant CSV parsing on every single keystroke.
**Action:** Implement singleton promise caching for asset fetching functions (`loadPrompts()`) with failure reset, and wrap search event listeners with a 150ms `debounce` handler to eliminate duplicate network traffic and main-thread DOM churn.
