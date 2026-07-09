## 2026-07-09 - Redundant Data Fetching in Event Handlers
**Learning:** The application was fetching and parsing the entire `prompts.csv` (113KB) and `vibeprompts.csv` (29KB) every time a user switched audiences or typed in the search bar. This led to unnecessary network traffic and main-thread blocking during expensive CSV parsing.
**Action:** Implemented a singleton promise pattern for data loading. This ensures the data is fetched and parsed exactly once, with subsequent callers awaiting the same cached promise. Added a reset mechanism on failure to allow for automatic retries.
