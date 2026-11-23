

# AmazonSponsoredBrandsAdData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adProduct** | [**AdProductEnum**](#AdProductEnum) |  |  |
|**brandEntityId** | **String** | The brand (Brand Registry entity) the campaign advertises. Sellers need one. |  [optional] |
|**bidOptimization** | **Boolean** | Amazon adjusts placement bids itself. Send false to set placementAdjustments. |  [optional] |
|**placementAdjustments** | [**List&lt;AmazonSponsoredBrandsCampaignDataPlacementAdjustmentsInner&gt;**](AmazonSponsoredBrandsCampaignDataPlacementAdjustmentsInner.md) | Only with bidOptimization false (400 otherwise). |  [optional] |
|**portfolioId** | **String** |  |  [optional] |
|**ad** | [**AmazonSponsoredBrandsAdDataAllOfAd**](AmazonSponsoredBrandsAdDataAllOfAd.md) |  |  [optional] |
|**defaultBid** | **BigDecimal** | Bid of the keywords and product targets without their own. With goal traffic (cost per click), US: 0.10 to 49, video 0.25 to 49. |  [optional] |
|**productTargets** | [**List&lt;AmazonSponsoredBrandsAdDataAllOfProductTargets&gt;**](AmazonSponsoredBrandsAdDataAllOfProductTargets.md) |  |  [optional] |
|**negativeProductTargets** | [**List&lt;AmazonSponsoredBrandsAdDataAllOfNegativeProductTargets&gt;**](AmazonSponsoredBrandsAdDataAllOfNegativeProductTargets.md) |  |  [optional] |



## Enum: AdProductEnum

| Name | Value |
|---- | -----|
| SPONSORED_BRANDS | &quot;SPONSORED_BRANDS&quot; |



