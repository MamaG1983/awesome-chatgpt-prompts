# Bolt's Performance Journal

## 2025-05-18 - Deduplicate `/prompts.csv` Network Requests and Parsing in `script.js`
**Learning:** `script.js` independently invoked `fetch("/prompts.csv")` and `parseCSV()` on page initialization (both in `initializeSearch` and `createPromptCards`) and repeatedly upon every audience toggle in `filterPrompts`. For a ~115KB CSV file, this triggered multiple redundant HTTP requests and repeated synchronous regex parsing passes on the main thread.
**Action:** Use a singleton promise cache (`getPrompts()`) that caches the fetched and parsed data across all calling functions, handles error resetting (`promptsCachePromise = null`), and ensures mutating operations like `.sort()` are performed on copied arrays rather than mutating the shared cache.
