## 2026-06-14 - Redundant Data Fetching in Static Site
**Learning:** The application was fetching and parsing the entire ~113KB prompts.csv file on every search keystroke and filter change. In static sites where data is loaded client-side via CSV/JSON, missing a caching layer for these assets leads to significant network overhead and UI lag during user interactions.
**Action:** Always implement a singleton promise or a simple caching mechanism for static data assets that are reused across different components or triggered by frequent user events like searching.
