

# UpdateAdSetRequestPlatformSpecificData

Platform-specific post-launch delivery settings. The platform is implied by the `platform` body param. Meta only; other platforms return 400. Unknown keys are rejected. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**optimizationGoal** | **String** | Meta ad-set optimization_goal (e.g. OFFSITE_CONVERSIONS, LANDING_PAGE_VIEWS). |  [optional] |
|**billingEvent** | **String** | Meta ad-set billing_event (e.g. IMPRESSIONS, LINK_CLICKS, THRUPLAY). |  [optional] |
|**startDate** | **String** | Ad set start_time (ISO 8601). |  [optional] |
|**endDate** | **String** | Ad set end_time (ISO 8601). |  [optional] |
|**dailyMinSpendTarget** | **BigDecimal** | Meta &#x60;daily_min_spend_target&#x60;: the least this ad set should spend per day, in whole currency units of the ad account. It reserves a share of a CAMPAIGN budget for one ad set, so it requires a campaign using Advantage campaign budget (CBO). On an ad set that owns its budget (ABO) this returns 409 — move the budget to the campaign with &#x60;PUT /v1/ads/campaigns/{campaignId}&#x60; first. Meta treats it as a target, not a guarantee, and rejects the combined minimum of a campaign&#39;s ad sets going over the campaign budget. Mutually exclusive with &#x60;lifetimeMinSpendTarget&#x60; (400): the flavour must match the campaign budget type, a daily budget takes a daily target. Read it back with &#x60;GET /v1/ads/ad-sets/{adSetId}?fields&#x3D;daily_min_spend_target&#x60;.  |  [optional] |
|**lifetimeMinSpendTarget** | **BigDecimal** | Meta &#x60;lifetime_min_spend_target&#x60;: the lifetime-budget flavour of &#x60;dailyMinSpendTarget&#x60;, in whole currency units. Send this one when the campaign budget is a lifetime budget. Same rules and same rejections.  |  [optional] |
|**promotedObject** | [**UpdateAdSetRequestPlatformSpecificDataPromotedObject**](UpdateAdSetRequestPlatformSpecificDataPromotedObject.md) |  |  [optional] |



