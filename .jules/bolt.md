## 2026-10-05 - Search String Pre-normalization Optimization
**Learning:** In real-time client-side search across prompt lists, calling `.toLowerCase()` repeatedly on array item properties (`act` and `prompt`) during every input event allocates strings dynamically on the main thread during typing bursts.
**Action:** Pre-compute lowercased properties (`actLower` and `promptLower`) once during dataset initialization so search filtering uses direct property access during keystrokes.
