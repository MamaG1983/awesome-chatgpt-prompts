## 2025-05-18 - $O(N \cdot M)$ DOM Card Audience Filter Bottleneck & Network Caching

**Learning:** In static sites with static CSV data sources like `prompts.csv`, calling `fetch()` and `parseCSV()` inside DOM event handlers causes repeated network requests and main-thread parsing lag. Furthermore, finding matching CSV data for each DOM card during visibility toggles runs in $O(N \cdot M)$ time.
**Action:** Use a singleton promise (`getPrompts()`) to cache fetched CSV promises, and tag DOM card elements with dataset attributes (`data-for-devs`) upon creation to enable $O(N)$ DOM visibility toggling.
