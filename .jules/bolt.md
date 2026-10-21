## 2026-10-21 - Variable Extraction Deduplication Overhead
**Learning:** Using `JSON.stringify` and `JSON.parse` with `Set` for deduplicating parsed variable objects in regex execution loops introduces significant string serialization overhead (~6x CPU time slowdown).
**Action:** Use an in-flight `Set` tracking variable names (`seenNames`) during regex iteration for O(1) duplicate checks and direct array accumulation.
