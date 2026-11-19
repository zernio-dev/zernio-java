

# AdMetricsResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stale** | **Boolean** | True when the analytics backend was over capacity and part of this answer came from a stored copy instead of a live read. |  |
|**staleSince** | **String** | With stale&#x3D;true: when the oldest stored copy used stopped being fresh. |  |
|**fromDate** | **String** |  |  |
|**toDate** | **String** |  |  |
|**backfillPending** | **Boolean** | True while older metrics for the window are still being fetched from the platform. |  |
|**missingIds** | **List&lt;String&gt;** | Asked ids that are not ads the caller can see. |  |



