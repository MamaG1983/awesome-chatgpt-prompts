## 2024-06-01 - [Optimized CSV fetching with promise-based caching]
**Learning:** In static sites that rely on CSV/JSON data fetched via JS, redundant fetch calls can occur during initialization and user interaction (like search). Caching the fetch promise instead of the raw data allows multiple simultaneous calls to resolve to the same request, preventing redundant network traffic and re-parsing.
**Action:** Always check if core data fetching can be centralized and cached via a singleton promise.
