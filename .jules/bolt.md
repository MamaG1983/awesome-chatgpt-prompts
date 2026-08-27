## 2026-08-27 - Cache CSV fetch and parse in Vibe Prompts search
**Learning:** `vibe/script.js` was invoking `loadPrompts()` on every `input` event during search typing, causing redundant network fetches of `vibeprompts.csv` and repeated CSV parsing operations for every typed character.
**Action:** Wrap CSV loading in a singleton promise (`cachedPromptsPromise`) in `loadPrompts()`, ensuring `vibeprompts.csv` is fetched and parsed only once per page session with automatic error reset for retries.
