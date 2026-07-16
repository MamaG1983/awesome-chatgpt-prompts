## 2024-05-22 - CSV Fetching & Parsing Bottleneck
**Learning:** Frequent re-fetching and re-parsing of static CSV files (prompts.csv and vibeprompts.csv) on every user interaction (search, filtering) causes unnecessary network overhead and main-thread blocking. Caching the result in a singleton promise ensures it happens only once per session.
**Action:** Use a singleton promise pattern for data fetching and parsing to provide a "cache" that is shared across all call sites, while handling failures and allowing retries.
