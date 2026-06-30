## 2026-06-30 - CSV Fetching Redundancy
**Learning:** The application was fetching and parsing static CSV data (prompts.csv and vibeprompts.csv) multiple times per session, notably during every keystroke in the vibe search and every audience switch on the main page.
**Action:** Implemented a singleton promise pattern to cache the result of the initial fetch and parse operation, ensuring subsequent calls return the same data without additional network or CPU overhead.
