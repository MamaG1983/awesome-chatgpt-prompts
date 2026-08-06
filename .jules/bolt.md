## 2024-03-31 - CSV Fetch and Parse Caching
**Learning:** Parsing the prompts CSV file on every keystroke or filter operation is highly inefficient (O(N) operations blocking the UI main thread). A singleton promise cache prevents redundant network requests and reparsing of the same static data.
**Action:** Use a global promise variable (`getPrompts` / `loadPrompts`) to fetch and parse the CSV only once. When resetting/sorting, clone the array to avoid mutating the cached singleton.
