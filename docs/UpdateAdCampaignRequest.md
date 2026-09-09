

# UpdateAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) | Required: platform campaign IDs are not globally unique. |  |
|**accountId** | **String** | **Meta only.** Zernio SocialAccount id owning the ad account. Needed only for an EMPTY campaign (zero ads); ignored otherwise. |  [optional] |
|**bidStrategy** | **BidStrategy** | **Meta + Google.** On Meta, the campaign default that ad sets inherit unless they override it. On Google, the campaign&#39;s own bidding strategy. On Google: LOWEST_COST_WITHOUT_CAP &#x3D; Maximize Conversions, COST_CAP + bidAmount &#x3D; Target CPA, LOWEST_COST_WITH_MIN_ROAS + roasAverageFloor &#x3D; Target ROAS, LOWEST_COST_WITH_BID_CAP + bidAmount &#x3D; Maximize Clicks with a CPC ceiling; portfolioBidStrategyId attaches a portfolio strategy instead. |  [optional] |
|**bidAmount** | **BigDecimal** | **Google only.** Whole currency units (USD: 12 &#x3D; $12.00). Max CPC for LOWEST_COST_WITH_BID_CAP, CPA target for COST_CAP; required for both. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | **Google only.** Decimal ROAS multiplier (2.0 &#x3D; 2.0x), required for LOWEST_COST_WITH_MIN_ROAS. |  [optional] |
|**portfolioBidStrategyId** | **String** | **Google only.** Attach an existing portfolio bid strategy (numeric id from GET /v1/ads/bid-strategies) instead of setting bidStrategy. Exclusive with bidStrategy. |  [optional] |
|**allowSharedBudgetUpdate** | **Boolean** | Google only. Explicitly allow changing a shared campaign budget, affecting every campaign that uses it. Does not bypass an unknown sharing state. |  [optional] |
|**budget** | [**UpdateAdCampaignRequestBudget**](UpdateAdCampaignRequestBudget.md) |  |  [optional] |
|**name** | **String** | **Meta only.** Rename the campaign. |  [optional] |
|**platformSpecificData** | [**UpdateAdCampaignRequestPlatformSpecificData**](UpdateAdCampaignRequestPlatformSpecificData.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| GOOGLE | &quot;google&quot; |



