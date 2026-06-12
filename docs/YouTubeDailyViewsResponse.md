

# YouTubeDailyViewsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**videoId** | **String** | The YouTube video ID |  [optional] |
|**durationSeconds** | **Integer** | Video length in seconds (from YouTube contentDetails.duration) |  [optional] |
|**dateRange** | [**YouTubeDailyViewsResponseDateRange**](YouTubeDailyViewsResponseDateRange.md) |  |  [optional] |
|**totalViews** | **Integer** | Sum of views across all days in the range |  [optional] |
|**dailyViews** | [**List&lt;YouTubeDailyViewsResponseDailyViewsInner&gt;**](YouTubeDailyViewsResponseDailyViewsInner.md) |  |  [optional] |
|**lastSyncedAt** | **OffsetDateTime** | When the data was last synced from YouTube |  [optional] |
|**scopeStatus** | [**YouTubeDailyViewsResponseScopeStatus**](YouTubeDailyViewsResponseScopeStatus.md) |  |  [optional] |



