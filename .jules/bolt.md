# Bolt's Performance Journal

## 2025-01-24 - CSV Loading and Parsing Optimization
**Learning:** Repetitive fetching and parsing of prompts.csv and vibeprompts.csv on user interactions (like search keystrokes and audience toggling) causes redundant network requests and blocks the main thread, resulting in noticeable UI lag. Implementing a singleton promise caching pattern resolves this by caching the parsed CSV data while allowing safe retry.
**Action:** Replace direct `fetch` calls in script.js and vibe/script.js with a cached, promise-based `getPrompts()` and `loadPrompts()` function.
