## 2026-08-17 - Singleton Promise Caching for Static CSV Fetches in Client-Side Search

**Learning:** Uncached `fetch` and parsing of static CSV files inside input event listeners (e.g., `loadPrompts()` in `vibe/script.js`) causes redundant network calls and main-thread CPU spikes on every single keystroke.
**Action:** Use a module-scoped singleton promise (`promptsPromise`) that caches the initial fetch and parse operation, with `.catch()` resetting the reference to `null` to allow retries on network failures.
