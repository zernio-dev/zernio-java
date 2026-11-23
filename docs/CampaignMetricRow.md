

# CampaignMetricRow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** |  |  |
|**adAccountId** | **String** |  |  |
|**campaignId** | **String** |  |  |
|**results** | **Map&lt;String, BigDecimal&gt;** | Without metrics, each uploaded result metric summed over the range, by metric key. |  [optional] |
|**name** | **String** | With metrics, the campaign name. null before its first sync. |  [optional] |
|**currency** | **String** | With metrics, the ad account currency every money metric of this campaign is in. Campaigns of different ad accounts are never summed together. |  [optional] |
|**metrics** | [**AdMetrics**](AdMetrics.md) | With metrics, only the asked metrics, summed over every ad of the campaign with rates recomputed from the sums. reach is deduplicated across the range for Meta and TikTok when the platform returns it. |  [optional] |
|**daily** | [**List&lt;CampaignMetricRowDailyInner&gt;**](CampaignMetricRowDailyInner.md) | With granularity&#x3D;day, one point per day with delivery, each carrying date and the asked metrics. |  [optional] |
|**lastSyncedAt** | **String** | With metrics, when the newest daily row of the campaign was synced. |  [optional] |



