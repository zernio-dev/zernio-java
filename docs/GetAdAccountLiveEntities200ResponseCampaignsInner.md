

# GetAdAccountLiveEntities200ResponseCampaignsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformCampaignId** | **String** |  |  [optional] |
|**campaignName** | **String** |  |  [optional] |
|**platformCampaignStatus** | **String** | Meta &#x60;effective_status&#x60; (ACTIVE, PAUSED, WITH_ISSUES...) or TikTok &#x60;secondary_status&#x60; (CAMPAIGN_STATUS_ENABLE...). |  [optional] |
|**configuredStatus** | **String** | The campaign&#39;s own switch: Meta &#x60;status&#x60; (ACTIVE, PAUSED, DELETED, ARCHIVED), or TikTok &#x60;operation_status&#x60; as ACTIVE (ENABLE) / PAUSED (DISABLE). |  [optional] |
|**status** | **String** | Zernio&#39;s normalized status (active, paused, ...), derived from &#x60;platformCampaignStatus&#x60;. |  [optional] |
|**budget** | [**GetAdAccountLiveEntities200ResponseCampaignsInnerBudget**](GetAdAccountLiveEntities200ResponseCampaignsInnerBudget.md) |  |  [optional] |
|**dailyBudget** | **BigDecimal** | Daily budget in whole units of &#x60;currency&#x60; (Meta &#x60;daily_budget&#x60;; TikTok &#x60;budget&#x60; under a daily budget mode). |  [optional] |
|**lifetimeBudget** | **BigDecimal** | Lifetime budget in whole units of &#x60;currency&#x60; (Meta &#x60;lifetime_budget&#x60;; TikTok &#x60;budget&#x60; under BUDGET_MODE_TOTAL). |  [optional] |
|**budgetMode** | **String** | TikTok only: &#x60;budget_mode&#x60; as TikTok reports it (BUDGET_MODE_DAY, BUDGET_MODE_DYNAMIC_DAILY_BUDGET, BUDGET_MODE_TOTAL, BUDGET_MODE_INFINITE). |  [optional] |
|**budgetRemaining** | **BigDecimal** | Meta &#x60;budget_remaining&#x60; in whole units of &#x60;currency&#x60;. Null when the campaign has no budget of its own, and always on TikTok. |  [optional] |
|**spendCap** | **BigDecimal** | Campaign spending limit (Meta &#x60;spend_cap&#x60;) in whole units of &#x60;currency&#x60;. Null when none is set, and always on TikTok. |  [optional] |
|**bidStrategy** | **String** | Meta &#x60;bid_strategy&#x60;, set on campaigns with a campaign budget. Null on TikTok. |  [optional] |



