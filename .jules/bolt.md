## 2024-06-17 - Redundant CSV Fetching and Parsing
**Learning:** The application fetches and parses large CSV files (`prompts.csv` and `vibeprompts.csv`) multiple times throughout its lifecycle. Specifically, in the Vibe section, the entire CSV is re-fetched and re-parsed on every search keystroke, leading to unnecessary network traffic and main-thread blocking during CPU-heavy parsing. The main application also performs redundant fetches during initial load and on every audience filter change.

**Action:** Implement promise-based caching (singleton promises) for CSV data fetching and parsing. This ensures that the data is fetched and processed exactly once per session, with subsequent consumers receiving the cached result immediately.
