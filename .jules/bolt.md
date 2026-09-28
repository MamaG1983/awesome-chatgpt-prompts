## 2026-09-28 - Avoid O(N*M) inner-loop string normalization during DOM matching
**Learning:** In `script.js`, DOM card generation and filtering repeatedly performed regex replacements (`.replace(/\s+/g, " ").replace(/[\n\r]/g, "").trim().toLowerCase()`) inside `Array.prototype.find` for every DOM element against the loaded CSV items.
**Action:** Pre-normalize prompt titles once when processing CSV data so inner-loop comparisons perform fast property equality and substring checks without repeated string allocations and regex parsing.
