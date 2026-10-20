# Bolt's Journal

## 2026-10-20 - Singleton Promise Caching & Field Pre-Computation in Static CSV Web Apps
**Learning:** In static Jekyll web apps where datasets like `prompts.csv` (~113KB) are fetched and searched dynamically in client-side JS (`script.js`), fetching and re-parsing CSV content across initial load, audience selection, and search input events causes redundant network requests and CPU overhead. Additionally, calling `.toLowerCase()` and regex replacements dynamically inside DOM loops ($O(N^2)$ matching between prompt cards and CSV items) creates noticeable main-thread lag.
**Action:** Use a singleton promise pattern (`getPrompts()`) to cache network requests and parsed objects, pre-compute search fields (`actLower`, `promptLower`, `cleanTitle`) during initialization, store attributes on rendered card elements (`data-for-devs`), and debounce search input listeners (150ms).
