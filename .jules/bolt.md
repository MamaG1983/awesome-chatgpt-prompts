# Bolt's Performance Journal

## 2025-02-17 - Redundant CSV Fetching and Parsing Bottlenecks
**Learning:** Parsing large CSV files like `prompts.csv` (~113KB) and `vibeprompts.csv` (~29KB) on every search input or audience toggle is extremely resource-intensive and blocks the main thread. Caching results using a singleton promise pattern (`getPrompts` / `loadPrompts`) avoids redundant network fetches and duplicate parsing operations while allowing retries if a fetch fails.
**Action:** Use a cached promise to load static files only once per session and reset the cache on failure to allow graceful retries.

## 2025-02-17 - Mutation of Shared Singleton Array Cache
**Learning:** When sorting or modifying a cached array loaded via a singleton promise pattern, direct mutations like `.sort()` affect all future consumers of that cached data, potentially leading to hard-to-debug layout or ordering issues.
**Action:** Always clone the cached array (e.g., `[...prompts]`) before applying any sorting or mutative array operations.

## 2025-02-17 - O(N^2) Nested Loop in DOM Filtering
**Learning:** Performing O(N * M) string matching on every card element during visibility toggles causes severe interface lag. Setting metadata (like `for_devs`) as a data attribute on the element during creation (`data-for-devs`) reduces the toggle complexity to O(N).
**Action:** Store item metadata on the DOM elements directly as custom `data-*` attributes during element creation, allowing O(N) lookups and toggling later.
