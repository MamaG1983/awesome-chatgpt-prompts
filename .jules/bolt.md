## 2025-05-18 - Deduplicating static CSV fetch and regex parsing with singleton promises

**Learning:** In static frontends like prompts.chat without state management frameworks, multiple distinct lifecycle and UI interaction functions (`initializeSearch`, `createPromptCards`, `filterPrompts`) independently fetched and parsed the same large CSV resource (`/prompts.csv`, ~115KB). Each call triggered full network transfers and CPU-intensive regex splitting on every audience toggle and search setup. Furthermore, mutating array sorts on shared data could introduce unintended side effects across callers.

**Action:** Consolidate data loading behind a singleton Promise getter (`getPrompts()`) that caches both the in-flight network request and parsed JavaScript object array, resetting the cache only on failure. Always shallow copy (`[...data]`) before in-place mutations like `.sort()` when handing cached collections to consumers.
