## 2025-05-18 - Avoid JSON Serialization for Object Array Deduplication
**Learning:** Using `[...new Set(array.map(v => JSON.stringify(v)))].map(v => JSON.parse(v))` in hot loops like `extractVariables` introduces significant string allocation and CPU overhead compared to tracking unique keys using a `Set` during matching.
**Action:** Always maintain a `Set` of key identifiers (e.g. `seenNames`) to filter duplicates in O(1) time while building the results array directly.
