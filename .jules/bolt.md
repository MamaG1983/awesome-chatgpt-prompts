## 2025-05-18 - Caching CSV Loads and Debouncing Input in Vibe Prompts

**Learning:** In static pages with multiple initializers (`renderMainPrompts`, `renderSidebarPrompts`, and `setupSearch`), calling `fetch()` and `parseCSV()` on each initialization and search event causes redundant network transfers and main thread thrashing on every keystroke. Using a singleton Promise cache (`promptsPromise`) ensures `fetch()` and CSV parsing happen exactly once per session while 150ms search input debouncing prevents main-thread thrashing on rapid keystrokes.
**Action:** Always wrap CSV/JSON file fetching logic in a singleton Promise pattern and apply debouncing to search input handlers when processing raw client-side datasets.
