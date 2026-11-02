

# YouTubeVideoRetentionResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**accountId** | **String** | The Zernio account ID for the YouTube account |  [optional] |
|**videoId** | **String** | The YouTube video ID |  [optional] |
|**title** | **String** | Video title |  [optional] |
|**publishedAt** | **OffsetDateTime** | When the video was published on YouTube |  [optional] |
|**durationSeconds** | **Integer** | Video length in seconds (from YouTube contentDetails.duration) |  [optional] |
|**dateRange** | [**YouTubeDailyViewsResponseDateRange**](YouTubeDailyViewsResponseDateRange.md) |  |  [optional] |
|**provisionalSince** | **LocalDate** | Present only when the range reaches into YouTube&#39;s ~3-day processing window: the first date whose numbers are provisional and may still be revised by YouTube. |  [optional] |
|**segmentMetricsAvailable** | **Boolean** | Whether YouTube returned startedWatching and stoppedWatching for this curve. When false, both are 0 placeholders in every point, not measured values. |  [optional] |
|**retentionCurve** | [**List&lt;YouTubeVideoRetentionResponseRetentionCurveInner&gt;**](YouTubeVideoRetentionResponseRetentionCurveInner.md) | Up to 100 points covering the video timeline, aggregated over the date range. Contains only the buckets YouTube reports for that range and is never zero-filled, so it can end before 1.0, skip positions, or be empty. |  [optional] |
|**note** | **String** | Present only when the curve is empty, explaining why |  [optional] |
|**scopeStatus** | [**YouTubeDailyViewsResponseScopeStatus**](YouTubeDailyViewsResponseScopeStatus.md) |  |  [optional] |



