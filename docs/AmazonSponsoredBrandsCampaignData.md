

# AmazonSponsoredBrandsCampaignData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adProduct** | [**AdProductEnum**](#AdProductEnum) |  |  |
|**brandEntityId** | **String** | The brand (Brand Registry entity) the campaign advertises. Sellers need one. |  [optional] |
|**bidOptimization** | **Boolean** | Amazon adjusts placement bids itself. Send false to set placementAdjustments. |  [optional] |
|**placementAdjustments** | [**List&lt;AmazonSponsoredBrandsCampaignDataPlacementAdjustmentsInner&gt;**](AmazonSponsoredBrandsCampaignDataPlacementAdjustmentsInner.md) | Only with bidOptimization false (400 otherwise). |  [optional] |
|**portfolioId** | **String** |  |  [optional] |



## Enum: AdProductEnum

| Name | Value |
|---- | -----|
| SPONSORED_BRANDS | &quot;SPONSORED_BRANDS&quot; |



