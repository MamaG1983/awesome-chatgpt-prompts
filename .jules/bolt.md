## 2025-01-05 - Repetitive CSV Fetching and Parsing Bottleneck
**Learning:** Parsing `prompts.csv` (~113KB) and `vibeprompts.csv` (~29KB) repeatedly on search input or filtering operations causes severe main-thread lag. Caching the parsed prompts via a singleton promise pattern eliminates redundant network requests and CPU overhead.
**Action:** Use a singleton promise cache for fetching and parsing CSV datasets, resetting the promise to `null` on failure so that retries are possible.
