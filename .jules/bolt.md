## 2026-05-30 - Centralized Prompt Data Fetching
**Learning:** Redundant fetching and parsing of large static assets (like a 113KB CSV) can lead to significant main thread blocking and unnecessary network overhead, especially during frequent UI updates like search.
**Action:** Always use a singleton promise pattern to cache asynchronous asset loading and parsing, ensuring expensive operations are performed only once per session.
