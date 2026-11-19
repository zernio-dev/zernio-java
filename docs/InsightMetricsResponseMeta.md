

# InsightMetricsResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | [**EntityEnum**](#EntityEnum) |  |  |
|**accountId** | **String** |  |  |
|**platformPostId** | **String** |  |  |
|**platform** | **String** |  |  |
|**granularity** | [**GranularityEnum**](#GranularityEnum) |  |  |
|**groupBy** | **String** | none, demographic, hour, keyword, or the Search Console dimensions grouped, such as query,country. |  |
|**timeframe** | [**TimeframeEnum**](#TimeframeEnum) | Instagram demographics: the period Instagram aggregated. |  |
|**fromDate** | **String** | Null for a lifetime or snapshot demographic breakdown. |  |
|**toDate** | **String** |  |  |
|**unavailableMetrics** | [**List&lt;InsightMetricsResponseMetaUnavailableMetricsInner&gt;**](InsightMetricsResponseMetaUnavailableMetricsInner.md) | Metrics asked that the platform could not answer for this account, with the reason. |  |
|**units** | [**Map&lt;String, InsightMetricsResponseMetaUnitsValue&gt;**](InsightMetricsResponseMetaUnitsValue.md) | Monetary metrics: the unit and currency the platform reports them in. Demographic metrics: count, share (0 to 1) or percent (0 to 100). |  |
|**dataDelay** | **String** | How late the platform reports these metrics, in words. Search Console: the rows cover final days only. |  |
|**provisionalSince** | **String** | First day the platform may still revise or have missing. Post insights only; null on account insights and when every day is final. |  |
|**stale** | **Boolean** | True when the platform refused the refresh and the answer is the last stored copy. |  |



## Enum: EntityEnum

| Name | Value |
|---- | -----|
| INSIGHTS | &quot;insights&quot; |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| TOTAL | &quot;total&quot; |
| DAY | &quot;day&quot; |



## Enum: TimeframeEnum

| Name | Value |
|---- | -----|
| THIS_WEEK | &quot;this_week&quot; |
| THIS_MONTH | &quot;this_month&quot; |



