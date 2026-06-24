# Bolt's Performance Journal

## 2025-05-15 - Redundant CSV Fetching and Parsing
**Learning:** The application was fetching and parsing `prompts.csv` (and `vibeprompts.csv`) on every search keystroke and during multiple initialization steps. For a large CSV file, this causes significant network overhead and blocks the main thread with expensive string manipulations and regex matching.
**Action:** Implemented a singleton promise pattern in `script.js` and `vibe/script.js` to cache the data after the first fetch. Subsequent requests return the same promise, ensuring the file is fetched and parsed exactly once.
