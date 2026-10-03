

# AdCampaign


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformCampaignId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**campaignName** | **String** |  |  [optional] |
|**status** | **AdStatus** | Delivery status derived from child ad statuses. Distinct from &#x60;reviewStatus&#x60;. |  [optional] |
|**reviewStatus** | **AdReviewStatus** |  |  [optional] |
|**platformCampaignStatus** | **String** | Raw platform-level campaign status (Meta &#x60;effective_status&#x60;; ChatGPT (OpenAI): the campaign&#39;s own switch, active / paused / archived; TikTok: the campaign&#39;s own switch &#x60;operation_status&#x60;, ENABLE / DISABLE). |  [optional] |
|**statusReadAt** | **OffsetDateTime** | Only on GET /v1/ads/campaigns with &#x60;live&#x3D;true&#x60;. When &#x60;platformCampaignStatus&#x60; was read from the platform; null when this campaign could not be read live. |  [optional] |
|**nativeSettings** | **Map&lt;String, Object&gt;** | TikTok only, only on GET /v1/ads/campaigns with &#x60;live&#x3D;true&#x60; and only on campaigns read live. TikTok&#39;s campaign/get record verbatim: operation_status, objective_type, budget_mode (BUDGET_MODE_INFINITE means no campaign budget, so budget lives on the ad groups), budget, and budget_optimize_on when TikTok returns it. Plus advertiser_currency and advertiser_timezone from TikTok&#39;s advertiser/info. |  [optional] |
|**configReadAt** | **OffsetDateTime** | Only on GET /v1/ads/campaigns with &#x60;live&#x3D;true&#x60;. When &#x60;nativeSettings&#x60; was read from the platform. Null whenever native settings were not read now. |  [optional] |
|**campaignIssuesInfo** | **List&lt;Object&gt;** | Platform-reported campaign issues (Meta &#x60;issues_info[]&#x60;). |  [optional] |
|**adCount** | **Integer** |  |  [optional] |
|**budget** | [**AdCampaignBudget**](AdCampaignBudget.md) |  |  [optional] |
|**campaignBudget** | [**AdCampaignBudget**](AdCampaignBudget.md) |  |  [optional] |
|**budgetLevel** | [**BudgetLevelEnum**](#BudgetLevelEnum) | Canonical CBO/ABO indicator. See AdTreeCampaign.budgetLevel. |  [optional] |
|**isBudgetScheduleEnabled** | **Boolean** | Meta-only. Mirrors Campaign.is_budget_schedule_enabled. |  [optional] |
|**currency** | **String** | ISO 4217 currency code for all budget amounts. Budgets are NOT normalized to USD. |  [optional] |
|**metrics** | [**AdMetrics**](AdMetrics.md) |  |  [optional] |
|**platformAdAccountId** | **String** |  |  [optional] |
|**platformAdAccountName** | **String** | Human-readable advertiser/account name from the platform. Refreshed on every sync. |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**advertisingChannelType** | **String** | Google-only. Raw campaign.advertising_channel_type. See AdTreeCampaign.advertisingChannelType. |  [optional] |
|**platformObjective** | **String** | Raw Meta campaign objective (e.g. OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_TRAFFIC) |  [optional] |
|**optimizationGoal** | **Object** |  |  [optional] |
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** | Representative bid from the top-spending ad set (whole currency units). Meta: populated when bidStrategy is LOWEST_COST_WITH_BID_CAP or COST_CAP. LinkedIn: the campaign unitCost, ungated, where 0 is a real delivery-stopping value. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | Representative ROAS floor from the top-spending ad set. Decimal multiplier (2.0 &#x3D; 2.0x). |  [optional] |
|**promotedObject** | [**AdTreeCampaignPromotedObject**](AdTreeCampaignPromotedObject.md) |  |  [optional] |
|**earliestAd** | **OffsetDateTime** |  |  [optional] |
|**latestAd** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| TIKTOK | &quot;tiktok&quot; |
| LINKEDIN | &quot;linkedin&quot; |
| PINTEREST | &quot;pinterest&quot; |
| GOOGLE | &quot;google&quot; |
| TWITTER | &quot;twitter&quot; |
| OPENAI | &quot;openai&quot; |



## Enum: BudgetLevelEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |



