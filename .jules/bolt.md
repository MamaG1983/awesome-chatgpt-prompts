## 2025-03-09 - Singleton Promise Caching for Static CSV Files

**Learning:** Repeated fetching and parsing of static data files (`/prompts.csv`) on UI interactions (like audience toggles or search filtering) creates redundant network calls and main-thread parsing overhead.
**Action:** Wrap network fetches for static assets in a singleton promise helper (`getPrompts()`) that caches the initial promise and resets on failure, ensuring network requests and parsing logic execute at most once.
