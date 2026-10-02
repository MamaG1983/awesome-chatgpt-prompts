## 2025-06-18 - Pre-computing Lowercase Strings for Array Filtering

**Learning:** Calling `.toLowerCase()` repeatedly inside an `Array.prototype.filter()` callback during real-time `input` events causes continuous garbage collection overhead and main-thread execution lag as dataset size grows.
**Action:** Pre-compute lowercased properties (`actLower` and `promptLower`) once during initialization/parsing, and query against pre-computed properties during real-time user search keystrokes.
