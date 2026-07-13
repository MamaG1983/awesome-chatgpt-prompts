## 2026-07-13 - Singleton Promise Cache Side Effects
**Learning:** When using a singleton promise to cache data shared across multiple UI components (like a parsed CSV array), mutations like `Array.prototype.sort()` within one component will affect all other consumers of that cached data. This can cause regressions if other components (like those using DOM-to-CSV index matching) expect a specific order.
**Action:** Always return a shallow copy or perform sorting on a clone (e.g., `[...await getPrompts()].sort()`) when the shared data needs to be ordered differently for different UI views.
