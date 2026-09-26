## 2026-09-26 - Singleton CSV Caching and O(1) Card Filtering

**Learning:** Repeatedly fetching and parsing `prompts.csv` and `vibeprompts.csv` on user keystrokes and audience toggles caused significant network and main-thread parsing overhead. Matching rendered cards back to parsed CSV items on every filter event created an O(N*M) DOM search bottleneck.
**Action:** Always cache CSV fetch/parse operations behind a singleton Promise pattern. Store filter metadata directly on rendered DOM nodes (e.g., `data-for-devs`) during initial card creation to reduce filter toggling to fast O(N) style updates.
