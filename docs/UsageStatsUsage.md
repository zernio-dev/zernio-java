

# UsageStatsUsage

Per-period usage counts. Fields present depend on `billingSystem`: Stripe returns `uploads` / `profiles` / `lastReset`; Metronome returns `connectedAccounts` / `xApiCalls` / `xApiCallsByOperation`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**uploads** | **Integer** | Stripe users only. Uploads consumed in the current period. |  [optional] |
|**profiles** | **Integer** | Stripe users only. Profiles currently owned. |  [optional] |
|**lastReset** | **OffsetDateTime** | Stripe users only. |  [optional] |
|**connectedAccounts** | **Integer** | Metronome users only. Accounts currently connected across the team. |  [optional] |
|**xApiCalls** | [**UsageStatsUsageXApiCalls**](UsageStatsUsageXApiCalls.md) |  |  [optional] |
|**xApiCallsByOperation** | **Map&lt;String, Integer&gt;** | Metronome users only. Per-operation X API call counts keyed by operation (e.g. &#x60;posts_read&#x60;, &#x60;content_create&#x60;, &#x60;content_create_with_url&#x60;). Resolve each key to price and metadata via &#x60;GET /v1/billing/x-pricing&#x60;. This is the canonical source — covers every price tier including the $0.200 URL tier that &#x60;xApiCalls&#x60; excludes.  |  [optional] |



