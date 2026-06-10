## 2025-05-15 - Redundant fetches in script.js and vibe/script.js
**Learning:** Multiple parts of the application fetch and parse the same CSV files independently. In `vibe/script.js`, the search functionality fetches and parses the CSV on every keystroke, which is extremely inefficient.
**Action:** Implement a singleton-like pattern for fetching and parsing prompts to ensure each CSV is only processed once per session.
