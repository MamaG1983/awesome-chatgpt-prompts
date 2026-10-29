## 2025-05-18 - CSV Re-fetching and DOM Traversal Bottlenecks in Prompt Filtering
**Learning:** Re-fetching and parsing `prompts.csv` on audience filter triggers and matching cards via inner HTML text traversals causes redundant network requests and O(N*M) DOM overhead on user interactions.
**Action:** Use a singleton promise (`getPrompts()`) to cache fetched CSV data and attach `data-for-devs` attributes directly onto prompt card DOM elements during creation for instant O(N) visibility toggles.
