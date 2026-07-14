## 2025-07-14 - Optimized CSV fetching using singleton promise pattern
**Learning:** Repeated fetching and parsing of static assets like CSV files in event listeners (search, filtering) causes unnecessary network traffic and main-thread overhead. Caching the result of the fetch as a promise (Singleton Promise Pattern) ensures the asset is only loaded and parsed once, while still being easily accessible via `await`.
**Action:** Use a singleton promise pattern for any frequently accessed static data in the frontend.
