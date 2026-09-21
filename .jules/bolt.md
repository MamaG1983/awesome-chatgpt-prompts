## 2026-09-21 - Singleton Data Caching and Dataset Tagging for Prompt Cards

**Learning:** Repeatedly fetching and parsing `prompts.csv` (~113KB) and `vibeprompts.csv` (~29KB) on user audience toggles or search events creates unnecessary network traffic and main-thread CSV parsing lag. Additionally, filtering prompt card DOM elements via O(N^2) inner text searching on each audience switch causes DOM thrashing.

**Action:** Wrap CSV fetching and parsing in singleton promises (`getPrompts()` and `loadPrompts()`) to ensure data is fetched and parsed only once per session. Tag DOM card elements during creation with `data-for-devs` attributes to enable O(N) direct attribute filtering when toggling audience modes.
