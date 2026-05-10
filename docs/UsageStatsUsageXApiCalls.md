

# UsageStatsUsageXApiCalls

**Deprecated.** Legacy 3-tier aggregate. Operations outside the three historical prices ($0.005/$0.010/$0.015) — notably the $0.200 \"Posts with URL\" tier added April 2026 — are silently excluded from this shape. Use `xApiCallsByOperation` instead; it captures every tier and is the source of truth for per-operation call counts. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**xApi005** | **Integer** | Calls at $0.005 per call (reads, lists, bookmarks, content manage, etc.) |  [optional] |
|**xApi010** | **Integer** | Calls at $0.010 per call (user reads, DM reads, follow reads, trends, list create, privacy update) |  [optional] |
|**xApi015** | **Integer** | Calls at $0.015 per call (posts/replies, DM sends, user interactions) |  [optional] |



