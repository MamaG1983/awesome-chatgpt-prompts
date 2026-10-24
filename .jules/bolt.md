## 2026-10-24 - Cache prompts.csv Network Fetch and O(N) Card Tag Filtering
**Learning:** Re-fetching `/prompts.csv` and re-running $O(N \times M)$ fuzzy string comparison loops over DOM cards during audience switching causes significant main-thread lag and redundant network calls.
**Action:** Use a singleton promise (`getPrompts()`) to cache fetched CSV data and attach `data-for-devs` attributes to prompt cards at DOM creation time, allowing $O(1)$ attribute lookups during audience toggling.
