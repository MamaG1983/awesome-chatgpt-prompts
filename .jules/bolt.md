## 2026-10-06 - Singleton Prompt CSV Fetching and Dataset Attribute Filtering

**Learning:** Repeatedly fetching and re-parsing `prompts.csv` (~114KB) on every filter operation or audience selector change created unnecessary network overhead and CPU processing. Additionally, matching card titles against CSV titles on every card toggle resulted in an expensive $O(N \times M)$ nested matching loop.

**Action:** Cache the CSV fetch/parse promise using a singleton promise pattern (`getPrompts()`) and tag prompt cards with `data-for-devs` attribute during initial creation, enabling $O(1)$ dataset attribute checks for visibility toggles.
