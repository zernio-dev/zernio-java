

# GetCampaignBidding200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) | campaign.advertising_channel_type. COST_CAP&#39;s underlying Google field differs by channel; see bidStrategy on PUT. |  [optional] |
|**biddingStrategyType** | **String** | Google&#39;s raw enum: MAXIMIZE_CONVERSIONS, TARGET_CPA, MAXIMIZE_CONVERSION_VALUE, TARGET_ROAS, TARGET_SPEND, MANUAL_CPC, TARGET_IMPRESSION_SHARE, or another Google adds later. |  [optional] |
|**bidSpec** | [**CampaignBiddingBidSpec**](CampaignBiddingBidSpec.md) |  |  [optional] |
|**portfolio** | [**CampaignBiddingPortfolio**](CampaignBiddingPortfolio.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this data was fetched from Google. Null when it was never served from cache. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s daily API quota was exhausted and this is the last successful fetch, not a live read. |  [optional] |
|**campaignId** | **String** |  |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| SEARCH | &quot;SEARCH&quot; |
| DISPLAY | &quot;DISPLAY&quot; |



