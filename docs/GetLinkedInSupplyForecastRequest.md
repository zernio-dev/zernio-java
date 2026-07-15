

# GetLinkedInSupplyForecastRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**adAccountId** | **String** |  |  |
|**spec** | [**TargetingSpec**](TargetingSpec.md) |  |  |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | Defaults to SPONSORED_UPDATES. |  [optional] |
|**timeRangeStart** | **Integer** | Unix ms. Must be in the future. |  |
|**timeRangeEnd** | **Integer** | Unix ms. Must be after start and within LinkedIn&#39;s max horizon. |  |
|**objectiveType** | **String** |  |  [optional] |
|**optimizationTarget** | **String** | When set, the forecast assumes auto-bidding. When unset, competingBid is required. |  [optional] |
|**dailyBudget** | **BigDecimal** | Either dailyBudget or totalBudget is required. |  [optional] |
|**totalBudget** | **BigDecimal** |  |  [optional] |
|**currency** | **String** | ISO 4217, defaults to USD. |  [optional] |
|**competingBid** | [**GetLinkedInSupplyForecastRequestCompetingBid**](GetLinkedInSupplyForecastRequestCompetingBid.md) |  |  [optional] |
|**enableAudienceNetwork** | **Boolean** | Defaults to false. Required true for connectedTelevisionOnly. |  [optional] |
|**enableAudienceExpansion** | **Boolean** | Defaults to false. |  [optional] |
|**connectedTelevisionOnly** | **Boolean** | Defaults to false. |  [optional] |



## Enum: CampaignTypeEnum

| Name | Value |
|---- | -----|
| SPONSORED_UPDATES | &quot;SPONSORED_UPDATES&quot; |
| SPONSORED_INMAILS | &quot;SPONSORED_INMAILS&quot; |
| DYNAMIC | &quot;DYNAMIC&quot; |



