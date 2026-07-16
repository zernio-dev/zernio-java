

# UpdateAdSetRequestPlatformSpecificData

Platform-specific post-launch delivery settings. The platform is implied by the `platform` body param. Meta only; other platforms return 400. Unknown keys are rejected. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**optimizationGoal** | **String** | Meta ad-set optimization_goal (e.g. OFFSITE_CONVERSIONS, LANDING_PAGE_VIEWS). |  [optional] |
|**billingEvent** | **String** | Meta ad-set billing_event (e.g. IMPRESSIONS, LINK_CLICKS, THRUPLAY). |  [optional] |
|**startDate** | **String** | Ad set start_time (ISO 8601). |  [optional] |
|**endDate** | **String** | Ad set end_time (ISO 8601). |  [optional] |
|**promotedObject** | [**UpdateAdSetRequestPlatformSpecificDataPromotedObject**](UpdateAdSetRequestPlatformSpecificDataPromotedObject.md) |  |  [optional] |



