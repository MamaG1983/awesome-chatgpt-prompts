## 2026-07-10 - CSV Fetch Caching
**Learning:** In a static site with large CSV data (~113KB), re-fetching and re-parsing data on every search keystroke or filter toggle causes significant main-thread lag and redundant network traffic. Using a singleton promise pattern for data loading ensures that fetching and parsing (including sorting) happens exactly once per session.
**Action:** Always implement a caching layer (like a singleton promise) for static data assets that are accessed frequently by user-driven events.
