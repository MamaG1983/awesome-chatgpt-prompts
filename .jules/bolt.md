## 2025-08-25 - Promise-based Singleton Caching for CSV Data Fetching

**Learning:** Uncached fetch operations in key user interaction paths (such as `input` search listeners and audience filter selectors) re-download and re-parse heavy CSV data synchronously/asynchronously on every user action or keystroke, creating noticeable main-thread lag and network redundancy.

**Action:** Wrap CSV fetching and parsing in singleton promise caches (`getPrompts()` in `script.js` and `loadPrompts()` in `vibe/script.js`) so that data is fetched and parsed at most once per session while allowing subsequent calls to resolve immediately.
