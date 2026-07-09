## 2026-07-09 - Singleton Promise for CSV Fetching
**Learning:** In a Jekyll project where data is fetched from CSV files for client-side search and rendering, redundant network requests can occur if each component or event listener (like 'input' for search) calls the fetch function independently. Using a singleton promise pattern ensures the file is only fetched and parsed once.
**Action:** Always implement a caching mechanism (like a singleton promise) for static data assets that are consumed by multiple listeners or rendered multiple times.
