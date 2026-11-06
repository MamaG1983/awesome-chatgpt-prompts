# Bolt's Journal - Critical Learnings

## 2026-11-06 - Singleton Promise Caching for Static CSV Assets
**Learning:** In static Jekyll applications with client-side CSV parsing, multiple independent components (`initializeSearch`, `createPromptCards`, and `filterPrompts`) triggered redundant full network fetches of `prompts.csv` (~115KB) and executed expensive regex parsing repeatedly on the main thread during initialization and audience toggles.
**Action:** Use a singleton promise pattern (`promptsCachePromise`) that caches both the in-flight network request and parsed prompt objects, while operating on shallow copies for sorting to avoid unintended mutation of shared cached data.
