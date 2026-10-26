## 2025-02-16 - Singleton CSV Promise Caching and Dataset Attribute Lookups

**Learning:** Re-fetching `/prompts.csv` and re-parsing it on every filter/toggle event in `script.js` caused unnecessary network and CPU overhead. Additionally, searching all CSV prompts for matching DOM titles during card visibility toggles created an O(cards * prompts) bottleneck with redundant string replacements.
**Action:** Use a `getPrompts()` singleton promise pattern to cache CSV fetching and parsing across functions, and store `dataset.forDevs` on DOM cards during creation for O(1) attribute checks during audience toggling.
