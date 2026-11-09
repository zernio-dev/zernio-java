

# YouTubeDailyViewsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**videoId** | **String** | The YouTube video ID |  [optional] |
|**durationSeconds** | **Integer** | Video length in seconds (from YouTube contentDetails.duration) |  [optional] |
|**dateRange** | [**YouTubeDailyViewsResponseDateRange**](YouTubeDailyViewsResponseDateRange.md) |  |  [optional] |
|**provisionalSince** | **LocalDate** | Present only when the range reaches into YouTube&#39;s ~3-day processing window: the first date whose numbers are provisional and may still be revised by YouTube. |  [optional] |
|**totalViews** | **Integer** | Sum of views across all days in the range |  [optional] |
|**stale** | **Boolean** | Present and true when YouTube refused the refresh (the Analytics quota or its rate limit) and the response serves the days Zernio already stored, so some days may be missing; lastSyncedAt says how old they are. Retry later for a full refresh. |  [optional] |
|**dailyViews** | [**List&lt;YouTubeDailyViewsResponseDailyViewsInner&gt;**](YouTubeDailyViewsResponseDailyViewsInner.md) |  |  [optional] |
|**lastSyncedAt** | **OffsetDateTime** | When the data was last synced from YouTube |  [optional] |
|**scopeStatus** | [**YouTubeDailyViewsResponseScopeStatus**](YouTubeDailyViewsResponseScopeStatus.md) |  |  [optional] |



