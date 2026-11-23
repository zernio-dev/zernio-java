

# AmazonSponsoredProductsAdData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adProduct** | [**AdProductEnum**](#AdProductEnum) |  |  |
|**targetingType** | [**TargetingTypeEnum**](#TargetingTypeEnum) | Required for a new campaign. MANUAL targets keywords and productTargets; AUTO lets Amazon match searches and products (tune them with autoTargeting). Immutable. |  [optional] |
|**biddingStrategy** | [**BiddingStrategyEnum**](#BiddingStrategyEnum) | Dynamic bidding: LEGACY_FOR_SALES lowers bids when a sale is unlikely, AUTO_FOR_SALES raises and lowers them (up to +100%), MANUAL keeps them fixed. |  [optional] |
|**placementBidding** | [**List&lt;AmazonSponsoredProductsCampaignDataPlacementBiddingInner&gt;**](AmazonSponsoredProductsCampaignDataPlacementBiddingInner.md) | Bid increase per placement, added on top of the bid (50 on a 1.00 bid gives 1.50 at the top of search). |  [optional] |
|**portfolioId** | **String** |  |  [optional] |
|**asins** | **List&lt;String&gt;** | Vendor profiles: the ASINs to advertise, one product ad each. |  [optional] |
|**skus** | **List&lt;String&gt;** | Seller profiles: the SKUs to advertise, one product ad each. Sending the identifier the profile does not use returns a 400. |  [optional] |
|**defaultBid** | **BigDecimal** | Required for a new ad group. Whole currency units; keywords and targets without their own bid use it. US: 0.02 to 1000. |  [optional] |
|**productTargets** | [**List&lt;AmazonSponsoredProductsAdDataAllOfProductTargets&gt;**](AmazonSponsoredProductsAdDataAllOfProductTargets.md) | MANUAL campaigns. Each entry is one Amazon targeting clause: a product (ASIN_SAME_AS), a category (ASIN_CATEGORY_SAME_AS) optionally refined by brand, price, rating or Prime in the same expression. |  [optional] |
|**negativeProductTargets** | [**List&lt;AmazonSponsoredProductsAdDataAllOfNegativeProductTargets&gt;**](AmazonSponsoredProductsAdDataAllOfNegativeProductTargets.md) |  |  [optional] |
|**autoTargeting** | [**AmazonSponsoredProductsAdDataAllOfAutoTargeting**](AmazonSponsoredProductsAdDataAllOfAutoTargeting.md) |  |  [optional] |



## Enum: AdProductEnum

| Name | Value |
|---- | -----|
| SPONSORED_PRODUCTS | &quot;SPONSORED_PRODUCTS&quot; |



## Enum: TargetingTypeEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;MANUAL&quot; |
| AUTO | &quot;AUTO&quot; |



## Enum: BiddingStrategyEnum

| Name | Value |
|---- | -----|
| LEGACY_FOR_SALES | &quot;LEGACY_FOR_SALES&quot; |
| AUTO_FOR_SALES | &quot;AUTO_FOR_SALES&quot; |
| MANUAL | &quot;MANUAL&quot; |



