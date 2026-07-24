

# AdTreeCampaign

Campaign with nested ad sets and rolled-up metrics

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformCampaignId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**campaignName** | **String** |  |  [optional] |
|**status** | **AdStatus** | Delivery status derived from child ad statuses. Distinct from &#x60;reviewStatus&#x60;, which reflects the platform-side review state. |  [optional] |
|**reviewStatus** | **AdReviewStatus** |  |  [optional] |
|**platformCampaignStatus** | **String** | Raw platform-level campaign status (Meta &#x60;effective_status&#x60;: ACTIVE, PAUSED, DELETED, ARCHIVED, IN_PROCESS, WITH_ISSUES). Distinct from per-ad &#x60;platformStatus&#x60;. |  [optional] |
|**campaignIssuesInfo** | **List&lt;Object&gt;** | Platform-reported campaign issues (Meta &#x60;issues_info[]&#x60;). Populated only when the platform has delivery issues to report; contains the specific error codes and messages. |  [optional] |
|**adCount** | **Integer** | Total ads across all ad sets |  [optional] |
|**adSetCount** | **Integer** |  |  [optional] |
|**budget** | [**AdTreeCampaignBudget**](AdTreeCampaignBudget.md) |  |  [optional] |
|**campaignBudget** | [**AdTreeCampaignCampaignBudget**](AdTreeCampaignCampaignBudget.md) |  |  [optional] |
|**budgetLevel** | [**BudgetLevelEnum**](#BudgetLevelEnum) | Canonical CBO/ABO indicator. &#x60;campaign&#x60; &#x3D; CBO (Advantage Campaign Budget, budget lives on the campaign). &#x60;adset&#x60; &#x3D; ABO (budget lives on each ad set). Route budget updates to the matching Meta entity. |  [optional] |
|**isBudgetScheduleEnabled** | **Boolean** | Meta-only. Mirrors Campaign.is_budget_schedule_enabled — true when the campaign uses budget scheduling (time-based budget changes). Independent of CBO/ABO. |  [optional] |
|**currency** | **String** | ISO 4217 currency code (e.g. USD, EUR, CLP, JPY) for all budget amounts in this campaign node. Budgets are NOT normalized to USD. |  [optional] |
|**metrics** | [**AdMetrics**](AdMetrics.md) |  |  [optional] |
|**platformAdAccountId** | **String** |  |  [optional] |
|**platformAdAccountName** | **String** | Human-readable advertiser/account name from the platform. Refreshed on every sync. |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**advertisingChannelType** | **String** | Google-only. Raw campaign.advertising_channel_type (SEARCH, PERFORMANCE_MAX, VIDEO, DEMAND_GEN, DISPLAY, SHOPPING, ...). Serving surface, distinct from platformObjective (advertiser intent). Null/absent for non-Google platforms. |  [optional] |
|**platformObjective** | **String** | Raw Meta campaign objective (e.g. OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_TRAFFIC) |  [optional] |
|**optimizationGoal** | **String** | Meta optimization goal shared across ad sets, or comma-separated values when ad sets differ (e.g. OFFSITE_CONVERSIONS, VALUE, LEAD_GENERATION) |  [optional] |
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** | Representative bid cap for the campaign — bubbled up from the top-spending ad set&#39;s &#x60;bid_amount&#x60; (whole currency units). Populated when the ad-set bidStrategy is LOWEST_COST_WITH_BID_CAP or COST_CAP. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | Representative ROAS floor for the campaign — bubbled up from the top-spending ad set. Decimal multiplier (2.0 &#x3D; 2.0x). |  [optional] |
|**promotedObject** | [**AdTreeCampaignPromotedObject**](AdTreeCampaignPromotedObject.md) |  |  [optional] |
|**adSets** | [**List&lt;AdTreeAdSet&gt;**](AdTreeAdSet.md) |  |  [optional] |
|**daily** | [**List&lt;AdDailyMetrics&gt;**](AdDailyMetrics.md) | Per-day metric series for this campaign. Present only when &#x60;GET /v1/ads/tree&#x60; is called with &#x60;timeIncrement&#x3D;1&#x60; (any &#x60;dailyLevel&#x60;). This is the per-campaign daily trend — summing its additive fields reproduces the campaign &#x60;metrics&#x60; total. |  [optional] |



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



