# Bolt's Performance Journal

## 2026-08-13 - Singleton Promise Caching for CSV Data Fetching
**Learning:** Repetitive fetching and parsing of `prompts.csv` and `vibeprompts.csv` on keystrokes and DOM state updates block the main thread and cause layout lag. Caching the fetch operation in a singleton promise solves this efficiently.
**Action:** Always use a singleton promise pattern for async resource loading and clone the cached results when applying operations like sorting.
