## 2026-06-07 - [Redundant CSV Fetches in Search]
**Learning:** In static Jekyll sites with heavy client-side logic (like this search-on-keystroke implementation), redundant CSV fetching and parsing can create a significant O(N) performance bottleneck for network and CPU, where N is the number of keystrokes.
**Action:** Always centralize data fetching with a promise-based singleton/cache to ensure assets are fetched and processed exactly once per session.
