

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
|**syncRequestedAccountIds** | **List&lt;String&gt;** | On a list of posts: the accounts this read queued for a fresh sync, because they were never synced or their stored numbers are over 90 minutes old. The answer holds the stored numbers; the synced ones arrive within minutes. |  [optional] |
|**analyticsOff** | [**List&lt;AnalyticsOffAccount&gt;**](AnalyticsOffAccount.md) | The X accounts read whose analytics sync does not run: their stored numbers are not refreshed, and their posts without any stay pending. On a list, on the first page. Absent when there are none, and on the groupBy and changedSince reads other than groupBy&#x3D;post. |  [optional] |
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



