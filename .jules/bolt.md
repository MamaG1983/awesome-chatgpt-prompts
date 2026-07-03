## 2026-07-03 - Singleton Promise for Data Fetching
**Learning:** In static sites that rely on client-side CSV/JSON parsing for search, redundant fetching and parsing on every input event (search keystroke) is a common bottleneck. Implementing a singleton promise pattern ensures that the data is fetched and parsed exactly once, even if multiple components or events trigger the load simultaneously.
**Action:** Use a cached promise (e.g., `getPrompts()`) instead of direct `fetch()` calls in event listeners and initialization routines.
