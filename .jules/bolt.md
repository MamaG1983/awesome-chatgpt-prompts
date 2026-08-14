# Bolt's Performance Journal ⚡

## 2025-01-05 - Initial Profiling and Memory Alignment
**Learning:** Found that repeated fetching and parsing of `/prompts.csv` (~113KB) and `/vibeprompts.csv` (~29KB) blocks the browser's main thread and generates redundant network traffic during search input events and audience switches. Introducing singleton promise caching resolves this completely. Additionally, inline HTML template handlers in `vibe/script.js` are vulnerable to unescaped quotes (e.g. apps named with `'` like "Player's plane"), which can be permanently solved by programmatically building search result items.
**Action:** Use a singleton promise pattern (`getPrompts()` / `loadPrompts()`) for both pages and refactor search sidebar generation to use programmatically created DOM elements instead of raw string interpolation.
