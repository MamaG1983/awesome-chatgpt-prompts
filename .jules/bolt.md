## 2026-06-19 - Centralized Data Fetching with Singleton Promises
**Learning:** The application was fetching and parsing large CSV files (prompts.csv) on every search input or audience filter change. This caused redundant network requests and expensive re-parsing of the entire dataset on the main thread, leading to UI jank.
**Action:** Use a singleton promise pattern to cache the data-fetching and parsing operation. By returning the same promise to all callers, we ensure the resource is loaded exactly once and shared efficiently across the search, filter, and initialization logic.
