# Bolt's Performance Journal ⚡

## 2025-05-18 - vibeprompts.csv In-Memory Fetch & Parse Caching
**Learning:** In the `/vibe` subpage, `loadPrompts()` was called multiple times on initial page load (both `renderMainPrompts` and `renderSidebarPrompts`) and repeatedly on every keystroke during `searchInput` event handling. Each invocation re-fetched `/vibeprompts.csv` over the network and re-executed regex-heavy CSV parsing on the main thread, causing unnecessary network bandwidth consumption and UI thread latency during typing.
**Action:** Cache the in-flight or resolved Promise of the parsed CSV data using a module-scoped variable (`promptsCachePromise`). Ensure errors reset the cached promise to allow retries, eliminating redundant network calls and repeated CSV parsing on every search keystroke.
