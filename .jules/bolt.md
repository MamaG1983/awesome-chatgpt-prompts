## 2026-08-22 - Singleton Promise Pattern for CSV Data Fetching & Parsing

**Learning:** Data fetching for `prompts.csv` (~113KB) and `vibeprompts.csv` (~29KB) was occurring multiple times on initial load, audience selector changes, and search input keystrokes. Using a singleton promise pattern (`getPrompts()` and `loadPrompts()`) guarantees that CSV fetching and parsing happen exactly once per session while sharing the result across all components.

**Action:** Wrap async data-fetching logic in a cached promise getter with error handling (resetting cache on error) and clone arrays when sorting to prevent mutating cached state.
