## 2026-09-03 - Singleton Promise Caching for Static CSV Datasets
**Learning:** In static Jekyll applications fetching large CSV files (`prompts.csv`), multiple features (search initialization, card creation, audience filtering) independently fetch and re-parse the CSV payload.
**Action:** Use a singleton promise (`getPrompts()`) that caches the initial fetch and `parseCSV` result, and clone array instances (`[...promptsData]`) before in-place sorting to preserve immutable cached state.
