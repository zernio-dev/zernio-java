

# AccountMetricsResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stale** | **Boolean** | True when the analytics backend was over capacity and part of this answer came from a stored copy instead of a live read. |  |
|**staleSince** | **String** | With stale&#x3D;true: when the oldest stored copy used stopped being fresh. |  |
|**entity** | [**EntityEnum**](#EntityEnum) |  |  |
|**granularity** | [**GranularityEnum**](#GranularityEnum) |  |  |
|**groupBy** | [**GroupByEnum**](#GroupByEnum) |  |  |
|**attribution** | [**AttributionEnum**](#AttributionEnum) |  |  |
|**fromDate** | **String** |  |  |
|**toDate** | **String** |  |  |



## Enum: EntityEnum

| Name | Value |
|---- | -----|
| ACCOUNTS | &quot;accounts&quot; |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| TOTAL | &quot;total&quot; |
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |



## Enum: GroupByEnum

| Name | Value |
|---- | -----|
| ACCOUNT | &quot;account&quot; |
| PLATFORM | &quot;platform&quot; |
| NONE | &quot;none&quot; |



## Enum: AttributionEnum

| Name | Value |
|---- | -----|
| PUBLISH | &quot;publish&quot; |
| RECEIVED | &quot;received&quot; |



