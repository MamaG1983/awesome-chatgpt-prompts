## 2026-07-07 - Singleton Promise Pattern for Data Assets
**Learning:** In static sites with dynamic filtering (like search or category toggles), fetching and parsing data assets (CSV/JSON) within event listeners leads to redundant network requests and CPU overhead.
**Action:** Implement a singleton promise pattern for data fetching. Cache the fetch/parse promise and return it for all subsequent calls. This ensures the asset is only loaded and processed once per session, even with rapid user interaction.
