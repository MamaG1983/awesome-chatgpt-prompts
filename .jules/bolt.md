## 2026-07-05 - Redundant Network Fetches in Subpages
**Learning:** Subpages (like `/vibe`) that implement their own data loading logic often miss global optimizations. In this codebase, `script.js` had an optimized `getPrompts()` singleton, but `vibe/script.js` was still performing a full CSV fetch and parse on every 'input' event during search.
**Action:** Always check subpage implementations for redundant data loading patterns. Use the singleton promise pattern for async data fetching to ensure assets are fetched and parsed exactly once per session.
