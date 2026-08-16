# Bolt's Journal - Critical Learnings

## 2026-08-16 - CSV Fetching & Parsing Singleton Pattern in Event Handlers
**Learning:** In client-side search implementations bound to real-time input events (e.g., `searchInput.addEventListener('input', ...)`), calling an uncached data fetcher function re-fetches and re-parses static CSV assets on every single keystroke (e.g., 30+ requests for a 15-character query).
**Action:** Always wrap static asset loaders (`vibeprompts.csv`, `prompts.csv`) in a singleton promise cache (`let promise = null;`) with error resetting to ensure network request and regex parsing happen exactly once per session.
