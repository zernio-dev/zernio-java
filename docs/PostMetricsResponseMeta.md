

# PostMetricsResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stale** | **Boolean** | True when the analytics backend was over capacity and part of this answer came from a stored copy instead of a live read. |  |
|**staleSince** | **String** | With stale&#x3D;true: when the oldest stored copy used stopped being fresh. |  |
|**entity** | [**EntityEnum**](#EntityEnum) |  |  |
|**granularity** | [**GranularityEnum**](#GranularityEnum) |  |  |
|**fromDate** | **String** |  |  |
|**toDate** | **String** |  |  |
|**missingIds** | **List&lt;String&gt;** | Ids asked that match no published post the caller can read. |  |
|**total** | **Integer** |  |  |
|**metricsSample** | [**PostMetricsResponseMetaAllOfMetricsSample**](PostMetricsResponseMetaAllOfMetricsSample.md) |  |  [optional] |



## Enum: EntityEnum

| Name | Value |
|---- | -----|
| POSTS | &quot;posts&quot; |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| TOTAL | &quot;total&quot; |
| DAY | &quot;day&quot; |



