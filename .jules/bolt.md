## 2026-07-11 - CSV Fetch and Parse Optimization
**Learning:** Repeated fetching and parsing of prompts.csv (~113KB) and vibeprompts.csv (~29KB) on every keystroke or audience toggle causes significant main-thread lag and unnecessary network overhead. DOM-based filtering by title-matching in O(N^2) complexity further degrades performance as the prompt list grows.
**Action:** Use a singleton promise pattern to cache the CSV fetch/parse result. Add metadata as data-attributes to DOM elements (e.g., `data-for-devs`) during initialization to enable O(N) visibility toggling.
