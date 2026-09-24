## 2025-06-18 - Vibe Prompts CSV Caching & Search Debouncing
**Learning:** `vibe/script.js` was fetching and parsing `vibeprompts.csv` on every search keystroke in `setupSearch()`, creating excessive network requests and unnecessary CSV parsing.
**Action:** Wrap `loadPrompts()` with a singleton promise pattern to cache the response across search keystrokes and debounce search input events with a 150ms delay.
