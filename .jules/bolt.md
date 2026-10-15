## 2025-05-18 - Variable Extraction Deduplication Overhead
**Learning:** `extractVariables` in `script.js` previously serialized objects via `JSON.stringify` and `JSON.parse` across a `Set` to deduplicate prompt variables, incurring unnecessary string allocations and O(N) array searching during modal updates and prompt rendering.
**Action:** Use a primitive `Set` (`seenNames`) during single-pass regex matching to deduplicate variables in O(1) time without object serialization overhead.
