## 2026-06-13 - [Cached Singleton Promises for Data Fetching]
**Learning:** In applications where large static data files (like `prompts.csv`) are fetched and parsed multiple times across different UI interactions (search, filter, initialization), centralizing the fetch into a cached singleton promise drastically reduces network overhead and re-parsing CPU time.
**Action:** Always check if core data files are being re-fetched on common user events like keystrokes or dropdown changes, and wrap the fetch in a memoized promise if they are.
