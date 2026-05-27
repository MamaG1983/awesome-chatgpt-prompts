## 2026-05-27 - [Singleton Pattern for Data Fetching]
**Learning:** In static sites with large data files (like CSVs), fetching and parsing data repeatedly during frequent UI events (like search) is a major performance bottleneck. Centralizing data access with a singleton promise prevents redundant network requests and CPU-intensive parsing.
**Action:** Always implement a centralized data loader with caching/singleton pattern when dealing with external data files that are used across multiple components or events.

## 2026-05-27 - [Map for O(1) DOM-to-Data Matching]
**Learning:** Matching DOM elements to data records using array searches (like `find`) inside loops creates O(N^2) complexity, which leads to jank during filtering or initialization of large lists.
**Action:** Pre-process data into a Map indexed by a normalized key to ensure O(1) lookups during UI updates.
