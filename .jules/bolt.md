## 2026-06-05 - [Singleton Promise Caching]
**Learning:** Redundant network requests and expensive parsing can be avoided by using a singleton promise for data fetching. In this Jekyll project, the CSV data was being fetched and parsed multiple times during search and filter operations.
**Action:** Always check for repeated `fetch()` or `parse()` calls on static data and consolidate them into a single promise-based getter.
