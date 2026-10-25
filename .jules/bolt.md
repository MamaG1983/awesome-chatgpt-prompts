# Bolt's Performance Journal

## 2025-06-18 - Singleton Promise Caching & DOM Metadata Toggling in script.js
**Learning:** Re-fetching `/prompts.csv` and re-parsing CSV text on every audience filter switch or search initialization causes redundant network calls and O(N*M) string matching across DOM elements. Pre-computing lowercase search fields (`actLower`, `promptLower`) during CSV parsing and attaching `data-for-devs` to prompt card DOM elements enables O(N) visibility toggling without repeated string search operations or redundant network/CSV parsing work.
**Action:** Always store metadata on created DOM nodes (`dataset`) when initial data is available and cache CSV fetches using a singleton promise pattern (`getPrompts()`).
