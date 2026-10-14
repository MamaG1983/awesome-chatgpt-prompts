## 2025-05-18 - Pre-compute Search Strings to Eliminate Keystroke Allocations
**Learning:** Calling `.toLowerCase()` on hundreds of prompt strings during `input` event filtering causes redundant string allocations and CPU work per keystroke.
**Action:** Pre-compute `actLower` and `promptLower` properties during search initialization so filtering operations can perform direct `String.prototype.includes` checks without string transformations.
