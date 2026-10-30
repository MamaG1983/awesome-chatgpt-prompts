## 2025-06-18 - CSV Fetch & Parse Caching with DOM Data Attributes

**Learning:** Repeatedly fetching and parsing CSV prompt data on user interactions (search input, audience toggling) caused redundant network requests and O(N^2) string matching loops when updating DOM card visibility.
**Action:** Use a singleton promise pattern for async resource fetching (`getPrompts()`) to guarantee single fetch/parse executions across session lifetime, tag DOM elements with data attributes (`data-for-devs`) during creation for O(1) state lookups, and always clone cached arrays (`[...cached].sort()`) before in-place sorting operations.
