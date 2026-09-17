## 2026-09-17 - Cached CSV Singleton Promise and Dataset Attribute Card Visibility Toggling

**Learning:** Re-fetching and re-parsing `prompts.csv` on audience switching or input triggers causes redundant HTTP calls and $O(N^2)$ fuzzy DOM title searches across prompt cards (~26.5ms for 100 iterations). Toggling visibility directly via a `data-for-devs` attribute set at creation reduces filtering time to <1ms ($O(N)$) and eliminates repeated CSV requests.
**Action:** Wrap CSV fetches in a singleton promise (`getPrompts()`) that resets to `null` on failure for retry support, and annotate prompt cards with DOM data attributes (`dataset.forDevs`) during creation for instant filtering.
