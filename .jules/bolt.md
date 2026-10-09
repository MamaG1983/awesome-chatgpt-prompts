## 2025-06-18 - Cached Prompt Fetching and Card Dataset Metadata

**Learning:** Re-fetching `/prompts.csv` and performing nested $O(N \times M)$ string search loops over DOM cards during audience switching creates significant main-thread frame drops.
**Action:** Use singleton promise caching (`getPrompts()`) for CSV fetching and store `data-for-devs` metadata directly on prompt cards during creation to allow $O(N)$ visibility toggling.
