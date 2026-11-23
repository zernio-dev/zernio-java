

# AdSetMetricRow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** |  |  |
|**adAccountId** | **String** |  |  |
|**campaignId** | **String** |  |  |
|**adSetId** | **String** |  |  |
|**name** | **String** | The ad set name. null before its first sync. |  |
|**currency** | **String** | The ad account currency every money metric of this ad set is in. Ad sets of different ad accounts are never summed together. |  |
|**metrics** | [**AdMetrics**](AdMetrics.md) | Only the asked metrics, summed over every ad of the ad set with rates recomputed from the sums. reach is deduplicated across the range for Meta and TikTok when the platform returns it. |  |
|**daily** | [**List&lt;CampaignMetricRowDailyInner&gt;**](CampaignMetricRowDailyInner.md) | With granularity&#x3D;day, one point per day with delivery, each carrying date and the asked metrics. |  [optional] |
|**lastSyncedAt** | **String** | When the newest daily row of the ad set was synced. |  |



