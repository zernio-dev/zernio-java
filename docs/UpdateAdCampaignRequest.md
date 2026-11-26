

# UpdateAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to stage this change instead of applying it. Nothing is written to the ad network; the response is &#x60;202&#x60; with the staged change and its diff. Apply it with POST /v1/ads/changes/{changeId}/confirm. Meta, Google, TikTok, X, Snapchat and Reddit; cannot be combined with &#x60;validateOnly&#x60; or &#x60;dryRun&#x60;. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Required: platform campaign IDs are not globally unique. |  |
|**accountId** | **String** | **Meta only.** Zernio SocialAccount id owning the ad account. Needed only for an EMPTY campaign (zero ads); ignored otherwise. |  [optional] |
|**bidStrategy** | **BidStrategy** | **Meta, Google and AppLovin.**  - Meta: the campaign default that ad sets inherit unless they override it. - Google: the campaign&#39;s own bidding strategy. LOWEST_COST_WITHOUT_CAP &#x3D; Maximize Conversions, COST_CAP + bidAmount &#x3D; Target CPA, LOWEST_COST_WITH_MIN_ROAS + roasAverageFloor &#x3D; Target ROAS, LOWEST_COST_WITH_BID_CAP + bidAmount &#x3D; Maximize Clicks with a CPC ceiling. - Google: portfolioBidStrategyId attaches a portfolio strategy instead. - AppLovin: sets the campaign goal value; the goal type itself cannot change. COST_CAP + bidAmount for a CPI, CPE or CPP goal, LOWEST_COST_WITH_MIN_ROAS + roasAverageFloor for a ROAS goal. - AppLovin app limits, checked before AppLovin is called: CPI below 200, CPE and CPP below 500, AD_ROAS at least 0.1, CHK_ROAS at least 0.01, BLD_ROAS at least 0.05. - AppLovin: a goal set per country, or the other goal family, is a 422.  |  [optional] |
|**bidAmount** | **BigDecimal** | **Google and AppLovin.** Whole currency units (USD: 12 &#x3D; $12.00). Google: max CPC for LOWEST_COST_WITH_BID_CAP, CPA target for COST_CAP; required for both. AppLovin: the CPI, CPE or CPP goal value, with COST_CAP. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | **Google and AppLovin.** Decimal ROAS multiplier (2.0 &#x3D; 2.0x), required for LOWEST_COST_WITH_MIN_ROAS. AppLovin: the ROAS goal value. |  [optional] |
|**portfolioBidStrategyId** | **String** | **Google only.** Attach an existing portfolio bid strategy (numeric id from GET /v1/ads/bid-strategies) instead of setting bidStrategy. Exclusive with bidStrategy. |  [optional] |
|**allowSharedBudgetUpdate** | **Boolean** | Google only. Explicitly allow changing a shared campaign budget (flagged as shared by Google, or used by more than one campaign), affecting every campaign that uses it. Does not bypass an unknown sharing state. Also required to move a campaign onto a shared budget with sharedBudgetId. |  [optional] |
|**targetImpressionShare** | [**GoogleTargetImpressionShare**](GoogleTargetImpressionShare.md) | Google Search only. Target impression share bidding. Exclusive with bidStrategy, portfolioBidStrategyId and manualCpc; bidAmount is refused alongside it (the ceiling is maxCpc). |  [optional] |
|**manualCpc** | [**GoogleManualCpc**](GoogleManualCpc.md) |  |  [optional] |
|**networkSettings** | [**GoogleNetworkSettings**](GoogleNetworkSettings.md) |  |  [optional] |
|**trackingUrlTemplate** | **String** | **Google only.** campaign.tracking_url_template; an empty string clears it. |  [optional] |
|**finalUrlSuffix** | **String** | **Google only.** campaign.final_url_suffix; an empty string clears it. |  [optional] |
|**sharedBudgetId** | **String** | **Google only.** Move the campaign onto this shared budget (id from GET /v1/ads/shared-budgets), or null to move it back onto a budget of its own sized by &#x60;budget&#x60;. |  [optional] |
|**budget** | [**UpdateAdCampaignRequestBudget**](UpdateAdCampaignRequestBudget.md) |  |  [optional] |
|**name** | **String** | **Meta, Reddit and AppLovin.** Rename the campaign. |  [optional] |
|**platformSpecificData** | [**UpdateAdCampaignRequestPlatformSpecificData**](UpdateAdCampaignRequestPlatformSpecificData.md) |  |  [optional] |



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
| REDDIT | &quot;reddit&quot; |
| MICROSOFT | &quot;microsoft&quot; |
| AMAZON | &quot;amazon&quot; |
| TRADEDESK | &quot;tradedesk&quot; |
| SNAPCHAT | &quot;snapchat&quot; |



