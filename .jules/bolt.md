## 2026-09-15 - Singleton Promise Caching & Debounced Input
**Learning:** Redundant CSV fetching and parsing during search keystrokes and audience toggling in Jekyll static apps causes unnecessary network requests and main-thread CPU spikes. Singleton promise caching prevents re-fetching while error reset allows retry handling.
**Action:** Always wrap CSV data loaders in a singleton promise and debounce live search event listeners by 150ms.
