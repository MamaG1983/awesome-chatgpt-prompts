## 2026-11-03 - Singleton Promise Pattern for Parallel Initializing Consumers

**Learning:** When multiple independent DOM setup routines (e.g., card generation and search index initialization) run concurrently upon `DOMContentLoaded`, each invoking asynchronous data fetching, standard function calls trigger duplicate network fetches and repeated CPU-intensive parsing on large assets (like `prompts.csv` at ~113KB). Furthermore, mutating operations like `.sort()` on shared cached arrays cause unintended ordering side effects across components unless cloned.

**Action:** Wrap shared asynchronous data fetching in a module-level singleton promise variable with error reset handling (`promptsPromise = null` in catch) to coalesce concurrent calls into a single in-flight request, and clone data arrays (`[...data]`) before performing in-place mutations like sorting.
