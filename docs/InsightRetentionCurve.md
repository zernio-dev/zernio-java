

# InsightRetentionCurve


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromDate** | **String** | fromDate when given; otherwise the publish date, so the curve covers the video lifetime. |  |
|**toDate** | **String** |  |  |
|**provisionalSince** | **String** |  |  |
|**durationSeconds** | **BigDecimal** |  |  |
|**segmentMetricsAvailable** | **Boolean** | False when YouTube has no startedWatching and stoppedWatching for the video; they read 0. |  |
|**points** | [**List&lt;InsightRetentionPoint&gt;**](InsightRetentionPoint.md) | Up to 100 points, ascending; empty when YouTube has no curve, as on videos with very few views. |  |



