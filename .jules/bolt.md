## 2025-07-04 - Singleton Promise for Data Fetching

**Learning:** Redundant network fetches and parsing of CSV data (100KB+) occurred on every search keystroke and audience toggle, causing unnecessary CPU and network load.
**Action:** Implemented a singleton promise pattern to cache the parsed data. This ensures the data is fetched and parsed exactly once per session, while still allowing for retries if the initial fetch fails.

## 2025-07-04 - Metadata Caching on DOM Elements

**Learning:** The prompt filtering logic was O(N^2) relative to the number of prompts, because it performed complex string normalization and lookups in the raw data for every card on every filter update.
**Action:** Stored the `for_devs` status as a `data-for-devs` attribute on the card during creation. This allows filtering to run in O(N) time with simple attribute lookups.
