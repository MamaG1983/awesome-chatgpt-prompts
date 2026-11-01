# Bolt's Journal - Critical Learnings

## 2026-11-01 - Singleton Promise Pattern for CSV Resource Caching
**Learning:** Both `script.js` and `vibe/script.js` loaded and parsed large CSV datasets (`prompts.csv` ~114KB, `vibeprompts.csv` ~29KB) multiple times across initial page load, audience toggles, and search events. Because network requests can resolve asynchronously and multiple components trigger loads on DOM readiness, simple variable caching can cause race conditions or duplicate initial fetches.
**Action:** Use a singleton promise pattern (`let cachePromise = null; if (!cachePromise) cachePromise = fetch(...)...; return cachePromise;`) with error reset (`.catch(() => cachePromise = null)`). Ensure consumers clone arrays (`[...prompts]`) before sorting to avoid mutating cached collections.
