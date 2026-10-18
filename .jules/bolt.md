## 2026-10-18 - Avoid JSON Serialization for Variable Deduplication in Parsing Pipelines
**Learning:** Using `JSON.stringify` and `JSON.parse` with `Set` to deduplicate objects in `extractVariables` introduces significant memory allocations and execution latency (~2.6x slower on repeated extractions).
**Action:** Use a `Set` of string identifiers (e.g. `seenNames`) alongside object insertion to maintain O(1) deduplication and optimal runtime performance.
