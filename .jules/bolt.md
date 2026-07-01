
## 2026-07-01 - Caching CSV fetches in Jekyll static sites
**Learning:** In a Jekyll-based static site where data is stored in CSV files, re-fetching and re-parsing these files on every UI interaction (like search or filtering) is a significant and easily avoidable performance bottleneck. Singleton promises are an effective pattern to ensure data is fetched and parsed only once per session.
**Action:** Always check for redundant fetch calls in event listeners and consolidate data loading into a cached promise pattern.
