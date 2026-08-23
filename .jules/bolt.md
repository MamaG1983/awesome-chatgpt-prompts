## 2026-08-23 - Singleton Promise Caching for CSV Data Fetching & Parsing

**Learning:** Repeated interactions (such as switching target audience or typing into search inputs) trigger redundant `fetch()` requests and expensive regex-based `parseCSV()` parsing for static assets like `prompts.csv` (~113KB) and `vibeprompts.csv` (~29KB). Using a singleton promise pattern (`getPrompts()`) ensures that network requests and CSV parsing execute strictly once per session, while resetting the promise on error ensures resilience. When returning cached arrays that may undergo sorting (`.sort()`), always clone the array first to avoid mutating shared state.

**Action:** Wrap static resource fetch and parse calls in a singleton promise function with error reset (`catch(() => promise = null)`) and always operate on array clones when sorting cached data.
