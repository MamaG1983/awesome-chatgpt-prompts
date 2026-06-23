## 2025-06-23 - Redundant CSV Fetching and Parsing
**Learning:** The application fetches and parses CSV data from the server on every search keystroke in some sections (vibe) and multiple times during initial load in others. For a static site, this data is constant and should be fetched once and cached in memory. Network requests on every keystroke are a major performance anti-pattern that can lead to UI lag and unnecessary server load.
**Action:** Use a singleton promise pattern for data fetching and parsing to ensure these operations happen exactly once per session.
