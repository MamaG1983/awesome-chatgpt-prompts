## 2026-08-18 - CSV Fetching & Parsing Cache Bottleneck in Vibe Prompts

**Learning:** In static Jekyll applications without state management frameworks, async utility functions like `loadPrompts()` called independently across components (`renderMainPrompts`, `renderSidebarPrompts`, search `input` event listeners) trigger redundant `fetch()` network requests and expensive CSV regex/split parsing on every user interaction (e.g., search keystrokes).
**Action:** Wrap CSV fetching and parsing routines in a singleton promise pattern (`promptsPromise`) with proper error handling (resetting to `null` on failure) to ensure network fetching and CSV parsing occur at most once per session.
