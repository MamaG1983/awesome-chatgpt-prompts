## 2026-06-28 - Caching static data fetches
**Learning:** Frequent UI interactions (search input, filter toggles) were triggering redundant 113KB CSV fetches and expensive parsing logic, blocking the main thread and wasting bandwidth.
**Action:** Implement a singleton promise pattern for data fetching. This ensures that concurrent or sequential requests for the same resource wait for a single underlying fetch/parse operation, making subsequent UI updates nearly instantaneous.
