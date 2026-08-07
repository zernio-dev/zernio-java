

# UpdateAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) | Required: platform campaign IDs are not globally unique. |  |
|**accountId** | **String** | **Meta only.** Zernio SocialAccount id owning the ad account. Needed only for an EMPTY campaign (zero ads); ignored otherwise. |  [optional] |
|**bidStrategy** | **BidStrategy** | **Meta + Google.** On Meta, the campaign default that ad sets inherit unless they override it. On Google, the campaign&#39;s own bidding strategy. |  [optional] |
|**bidAmount** | **BigDecimal** | **Google only.** Whole currency units (USD: 12 &#x3D; $12.00). Max CPC for LOWEST_COST_WITH_BID_CAP, CPA target for COST_CAP; required for both. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | **Google only.** Decimal ROAS multiplier (2.0 &#x3D; 2.0x), required for LOWEST_COST_WITH_MIN_ROAS. |  [optional] |
|**budget** | [**UpdateAdCampaignRequestBudget**](UpdateAdCampaignRequestBudget.md) |  |  [optional] |
|**name** | **String** | **Meta only.** Rename the campaign. |  [optional] |
|**platformSpecificData** | [**UpdateAdCampaignRequestPlatformSpecificData**](UpdateAdCampaignRequestPlatformSpecificData.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| GOOGLE | &quot;google&quot; |



