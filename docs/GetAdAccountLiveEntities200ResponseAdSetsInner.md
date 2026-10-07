

# GetAdAccountLiveEntities200ResponseAdSetsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformAdSetId** | **String** |  |  [optional] |
|**adSetName** | **String** |  |  [optional] |
|**platformCampaignId** | **String** |  |  [optional] |
|**platformAdSetStatus** | **String** | Meta &#x60;effective_status&#x60; (ACTIVE, PAUSED, CAMPAIGN_PAUSED...) or TikTok &#x60;secondary_status&#x60; (ADGROUP_STATUS_DELIVERY_OK, ADGROUP_STATUS_AUDIT...). |  [optional] |
|**configuredStatus** | **String** | The ad set&#39;s own switch: Meta &#x60;status&#x60;, or TikTok &#x60;operation_status&#x60; as ACTIVE / PAUSED. |  [optional] |
|**status** | **String** | Zernio&#39;s normalized status, derived from &#x60;platformAdSetStatus&#x60;. |  [optional] |
|**budget** | [**GetAdAccountLiveEntities200ResponseAdSetsInnerBudget**](GetAdAccountLiveEntities200ResponseAdSetsInnerBudget.md) |  |  [optional] |
|**dailyBudget** | **BigDecimal** | Daily budget in whole units of &#x60;currency&#x60;. |  [optional] |
|**lifetimeBudget** | **BigDecimal** | Lifetime budget in whole units of &#x60;currency&#x60;. |  [optional] |
|**budgetMode** | **String** | TikTok only: &#x60;budget_mode&#x60; as TikTok reports it. |  [optional] |
|**budgetRemaining** | **BigDecimal** | Meta &#x60;budget_remaining&#x60; in whole units of &#x60;currency&#x60;. Null when the ad set has no budget of its own, and always on TikTok. |  [optional] |
|**bidStrategy** | **String** | Meta &#x60;bid_strategy&#x60;. On TikTok the ad group&#39;s &#x60;bid_type&#x60; normalized to the same vocabulary (LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, LOWEST_COST_WITH_MIN_ROAS). |  [optional] |
|**bidAmount** | **BigDecimal** | Bid cap or cost target in whole units of &#x60;currency&#x60; (Meta &#x60;bid_amount&#x60;; TikTok &#x60;bid_price&#x60;, else &#x60;conversion_bid_price&#x60;, else &#x60;deep_cpa_bid&#x60;). Null when the strategy has none. |  [optional] |
|**optimizationGoal** | **String** | Meta or TikTok &#x60;optimization_goal&#x60;. |  [optional] |
|**billingEvent** | **String** | Meta or TikTok &#x60;billing_event&#x60;. |  [optional] |
|**promotedObject** | **Map&lt;String, Object&gt;** | Meta &#x60;promoted_object&#x60; verbatim (snake_case). On TikTok &#x60;{ pixelId, customEventType, applicationId, customConversionId }&#x60; from &#x60;pixel_id&#x60;, &#x60;optimization_event&#x60;, &#x60;app_id&#x60; and &#x60;custom_conversion_id&#x60;, only the keys TikTok has set; null when none is. |  [optional] |
|**targeting** | **Map&lt;String, Object&gt;** | The platform&#39;s targeting verbatim (snake_case), as it reports it now: Meta &#x60;targeting&#x60;, or TikTok&#39;s ad group targeting fields (location_ids, age_groups, gender, languages, interest_category_ids, audience_ids, placements...). |  [optional] |
|**schedule** | [**GetAdAccountLiveEntities200ResponseAdSetsInnerSchedule**](GetAdAccountLiveEntities200ResponseAdSetsInnerSchedule.md) |  |  [optional] |



