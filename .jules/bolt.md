## 2026-05-26 - [Performance Bottleneck: Redundant CSV Fetching and Parsing]
**Learning:** The application was fetching and parsing the entire `prompts.csv` (113KB) on every search keystroke and every time "Developer Mode" was toggled. Additionally, it was using $O(N^2)$ logic to match DOM elements with CSV data, leading to noticeable UI lag as the prompt collection grows.

**Action:** Implement a singleton pattern for data loading (`loadPrompts`) and use a `Map` for $O(1)$ lookups. Pre-normalize search keys during the initial parsing phase to minimize per-keystroke CPU overhead.
