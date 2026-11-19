

# InboxMetricsResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stale** | **Boolean** | True when the analytics backend was over capacity and part of this answer came from a stored copy instead of a live read. |  |
|**staleSince** | **String** | With stale&#x3D;true: when the oldest stored copy used stopped being fresh. |  |
|**entity** | [**EntityEnum**](#EntityEnum) |  |  |
|**granularity** | [**GranularityEnum**](#GranularityEnum) |  |  |
|**groupBy** | **List&lt;String&gt;** |  |  |
|**fromDate** | **String** |  |  |
|**toDate** | **String** |  |  |
|**total** | **Integer** | With groupBy&#x3D;conversation and include&#x3D;total: the conversations the list holds, up to 100,000. |  |
|**totalIsCapped** | **Boolean** | true when the conversation list holds more than 100,000 conversations. |  |



## Enum: EntityEnum

| Name | Value |
|---- | -----|
| INBOX | &quot;inbox&quot; |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| TOTAL | &quot;total&quot; |
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |



