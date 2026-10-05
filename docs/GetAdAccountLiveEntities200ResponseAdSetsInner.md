

# GetAdAccountLiveEntities200ResponseAdSetsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformAdSetId** | **String** |  |  [optional] |
|**adSetName** | **String** |  |  [optional] |
|**platformCampaignId** | **String** |  |  [optional] |
|**platformAdSetStatus** | **String** | Meta &#x60;effective_status&#x60;, for example ACTIVE, PAUSED, CAMPAIGN_PAUSED. |  [optional] |
|**configuredStatus** | **String** | Meta &#x60;status&#x60;: the ad set&#39;s own switch. |  [optional] |
|**status** | **String** | Zernio&#39;s normalized status, derived from &#x60;platformAdSetStatus&#x60;. |  [optional] |
|**budget** | [**GetAdAccountLiveEntities200ResponseAdSetsInnerBudget**](GetAdAccountLiveEntities200ResponseAdSetsInnerBudget.md) |  |  [optional] |
|**dailyBudget** | **BigDecimal** | Meta &#x60;daily_budget&#x60; in whole units of &#x60;currency&#x60;. |  [optional] |
|**lifetimeBudget** | **BigDecimal** | Meta &#x60;lifetime_budget&#x60; in whole units of &#x60;currency&#x60;. |  [optional] |
|**budgetRemaining** | **BigDecimal** | Meta &#x60;budget_remaining&#x60; in whole units of &#x60;currency&#x60;. Null when the ad set has no budget of its own. |  [optional] |
|**bidStrategy** | **String** | Meta &#x60;bid_strategy&#x60;. |  [optional] |
|**bidAmount** | **BigDecimal** | Meta &#x60;bid_amount&#x60; (bid cap or cost target) in whole units of &#x60;currency&#x60;. Null when the strategy has none. |  [optional] |
|**optimizationGoal** | **String** | Meta &#x60;optimization_goal&#x60;. |  [optional] |
|**billingEvent** | **String** | Meta &#x60;billing_event&#x60;. |  [optional] |
|**promotedObject** | **Map&lt;String, Object&gt;** | Meta &#x60;promoted_object&#x60; verbatim (snake_case). |  [optional] |
|**targeting** | **Map&lt;String, Object&gt;** | Meta &#x60;targeting&#x60; verbatim (snake_case), as Meta returns it now. |  [optional] |
|**schedule** | [**GetAdAccountLiveEntities200ResponseAdSetsInnerSchedule**](GetAdAccountLiveEntities200ResponseAdSetsInnerSchedule.md) |  |  [optional] |



