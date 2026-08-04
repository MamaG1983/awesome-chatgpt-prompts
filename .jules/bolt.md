# Bolt's Performance Journal

## 2025-01-10 - [Singleton Promise Cache for Prompts CSV]
**Learning:** Repeatedly fetching and parsing `prompts.csv` and `vibeprompts.csv` on search inputs, audience toggles, and card initialization triggers duplicate network requests and high CPU load due to regex-based CSV parsing. Implementing a singleton promise pattern caches the parsed results, while cloning arrays during sorting avoids side-effects on the shared cache.
**Action:** Use a singleton promise pattern for loading CSV data. When sorting the cached array, clone it (e.g. `[...await getPrompts()].sort()`) to prevent mutating the shared cache.
