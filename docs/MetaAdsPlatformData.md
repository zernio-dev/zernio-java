

# MetaAdsPlatformData

Meta (facebook/instagram) options for platformSpecificData on POST /v1/ads/boost and /v1/ads/create. Unknown keys are rejected, not dropped.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** | Whole currency units (USD: 5 &#x3D; $5.00). Required when bidStrategy is LOWEST_COST_WITH_BID_CAP or COST_CAP. May also be sent alone, WITHOUT bidStrategy, to set the cap on an ad set joining a COST_CAP / LOWEST_COST_WITH_BID_CAP campaign (the strategy is inherited from the campaign). On POST /v1/ads/create that shape requires existingCampaignId and is a 400 otherwise; on POST /v1/ads/boost it is promoted to LOWEST_COST_WITH_BID_CAP. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | Decimal ROAS multiplier (2.0 &#x3D; 2.0x). Required when bidStrategy is LOWEST_COST_WITH_MIN_ROAS; sending it without bidStrategy is a 400. |  [optional] |



