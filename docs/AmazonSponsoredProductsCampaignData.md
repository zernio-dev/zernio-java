

# AmazonSponsoredProductsCampaignData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adProduct** | [**AdProductEnum**](#AdProductEnum) |  |  |
|**targetingType** | [**TargetingTypeEnum**](#TargetingTypeEnum) | Required for a new campaign. MANUAL targets keywords and productTargets; AUTO lets Amazon match searches and products (tune them with autoTargeting). Immutable. |  [optional] |
|**biddingStrategy** | [**BiddingStrategyEnum**](#BiddingStrategyEnum) | Dynamic bidding: LEGACY_FOR_SALES lowers bids when a sale is unlikely, AUTO_FOR_SALES raises and lowers them (up to +100%), MANUAL keeps them fixed. |  [optional] |
|**placementBidding** | [**List&lt;AmazonSponsoredProductsCampaignDataPlacementBiddingInner&gt;**](AmazonSponsoredProductsCampaignDataPlacementBiddingInner.md) | Bid increase per placement, added on top of the bid (50 on a 1.00 bid gives 1.50 at the top of search). |  [optional] |
|**portfolioId** | **String** |  |  [optional] |



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



