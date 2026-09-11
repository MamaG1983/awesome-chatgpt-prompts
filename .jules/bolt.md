# Bolt's Journal

## 2026-09-11 - Prompts CSV Caching and O(N) Card Visibility Filtering
**Learning:** `script.js` was triggering multiple fetches and parses of `prompts.csv` across initial search setup, audience filtering, and card creation. On audience switching, `filterPrompts()` was performing an O(N*M) loop re-matching every card's DOM title against CSV entries using multi-line regex string normalizations.
**Action:** Use a singleton promise pattern (`getPrompts()`) to cache `prompts.csv` parsing across all functions, and tag cards with `data-for-devs` attributes on initial creation to reduce audience filtering time to O(N) direct dataset checks.
