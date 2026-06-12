

# YouTubeVideoRetentionResponseRetentionCurveInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elapsedVideoTimeRatio** | **BigDecimal** | Position in the video as a ratio (0.01-1.0, exclusive end of each interval) |  [optional] |
|**audienceWatchRatio** | **BigDecimal** | Absolute share of viewers watching at this point. Can exceed 1 (rewinds/looping, common on Shorts). |  [optional] |
|**relativeRetentionPerformance** | **BigDecimal** | Retention vs videos of similar length (0 &#x3D; worst, 0.5 &#x3D; median, 1 &#x3D; best) |  [optional] |
|**startedWatching** | **Integer** | Viewers who started watching in this segment |  [optional] |
|**stoppedWatching** | **Integer** | Viewers who stopped watching in this segment |  [optional] |
|**totalSegmentImpressions** | **Integer** | Total views of this segment, including rewatches |  [optional] |



