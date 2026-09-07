

# CampaignBidding

A Google campaign's current bidding, mapped onto the same triplet PUT /v1/ads/campaigns/{campaignId} accepts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) | campaign.advertising_channel_type. COST_CAP&#39;s underlying Google field differs by channel; see bidStrategy on PUT. |  [optional] |
|**biddingStrategyType** | **String** | Google&#39;s raw enum: MAXIMIZE_CONVERSIONS, TARGET_CPA, MAXIMIZE_CONVERSION_VALUE, TARGET_ROAS, TARGET_SPEND, MANUAL_CPC, TARGET_IMPRESSION_SHARE, or another Google adds later. |  [optional] |
|**bidSpec** | [**CampaignBiddingBidSpec**](CampaignBiddingBidSpec.md) |  |  [optional] |
|**portfolio** | [**CampaignBiddingPortfolio**](CampaignBiddingPortfolio.md) |  |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| SEARCH | &quot;SEARCH&quot; |
| DISPLAY | &quot;DISPLAY&quot; |



