

# GetCampaignAdSchedule200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignId** | **String** |  |  [optional] |
|**schedule** | [**List&lt;AdScheduleWindow&gt;**](AdScheduleWindow.md) |  |  [optional] |
|**servesAroundTheClock** | **Boolean** | True when the campaign carries no ad schedule at all, so it can serve at any time. |  [optional] |
|**cachedAt** | **OffsetDateTime** |  |  [optional] |
|**stale** | **Boolean** | True when a quota-exhausted read served the last-good copy. |  [optional] |
|**performance** | [**GetCampaignAdSchedule200ResponsePerformance**](GetCampaignAdSchedule200ResponsePerformance.md) |  |  [optional] |



