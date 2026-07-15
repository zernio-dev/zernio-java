

# GetLinkedInBidPricingRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio social account ID (LinkedIn). |  |
|**adAccountId** | **String** | LinkedIn ad account ID (numeric). |  |
|**spec** | [**TargetingSpec**](TargetingSpec.md) | Same targeting spec used by POST /v1/ads/create. |  |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | Defaults to SPONSORED_UPDATES. |  [optional] |
|**bidType** | [**BidTypeEnum**](#BidTypeEnum) | Defaults to CPM. |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | Defaults to EXACT. |  [optional] |
|**currency** | **String** | ISO 4217, defaults to USD. |  [optional] |
|**objectiveType** | **String** | LinkedIn objectiveType, e.g. WEBSITE_VISIT, LEAD_GENERATION, VIDEO_VIEW. |  [optional] |
|**optimizationTargetType** | **String** | LinkedIn optimizationTargetType, e.g. MAX_CLICK, MAX_IMPRESSION. |  [optional] |
|**dailyBudget** | **BigDecimal** | Optional daily budget in whole account-currency units. LinkedIn refines the suggested bid to this budget. |  [optional] |



## Enum: CampaignTypeEnum

| Name | Value |
|---- | -----|
| TEXT_AD | &quot;TEXT_AD&quot; |
| SPONSORED_UPDATES | &quot;SPONSORED_UPDATES&quot; |
| SPONSORED_INMAILS | &quot;SPONSORED_INMAILS&quot; |



## Enum: BidTypeEnum

| Name | Value |
|---- | -----|
| CPM | &quot;CPM&quot; |
| CPC | &quot;CPC&quot; |
| CPV | &quot;CPV&quot; |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;EXACT&quot; |
| AUDIENCE_EXPANDED | &quot;AUDIENCE_EXPANDED&quot; |



