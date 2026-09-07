

# CampaignBiddingBidSpec

Null when the campaign is on a strategy PUT does not model (Manual CPC, Target Impression Share, ...); show biddingStrategyType instead in that case.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** | Whole currency units. Present for COST_CAP and LOWEST_COST_WITH_BID_CAP, and omitted when the campaign is on a bare TARGET_SPEND with no CPC ceiling set. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | Decimal ROAS multiplier (2.0 &#x3D; 2.0x). Present for LOWEST_COST_WITH_MIN_ROAS. |  [optional] |
|**portfolioBidStrategyId** | **String** | Present alone (bidStrategy omitted) when the campaign is on a portfolio strategy; see portfolio. |  [optional] |



