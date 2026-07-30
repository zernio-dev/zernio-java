

# InstagramAccountInsightsResponse

Shared account-insights response envelope used by every platform-level analytics endpoint (/v1/analytics/{facebook|instagram|youtube|linkedin|tiktok}/_*). The name is historical - the shape was first shipped for Instagram and every new platform endpoint reuses it for response-shape consistency. The platform field echoes back which platform served the response. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**accountId** | **String** | The Zernio SocialAccount ID |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform that served this response. |  [optional] |
|**dateRange** | [**InstagramAccountInsightsResponseDateRange**](InstagramAccountInsightsResponseDateRange.md) |  |  [optional] |
|**metricType** | [**MetricTypeEnum**](#MetricTypeEnum) |  |  [optional] |
|**breakdown** | **String** | Breakdown dimension used (only present when breakdown was requested) |  [optional] |
|**metrics** | [**Map&lt;String, InstagramAccountInsightsResponseMetricsValue&gt;**](InstagramAccountInsightsResponseMetricsValue.md) | Object keyed by metric name. For time_series: each metric has \&quot;total\&quot; (number) and \&quot;values\&quot; (array of {date, value}). For total_value: each metric has \&quot;total\&quot; (number) and optionally \&quot;breakdowns\&quot; (array of {dimension, value}).  Monetary metrics additionally carry \&quot;unit\&quot; and \&quot;currency\&quot;. Zernio never rescales money: \&quot;total\&quot; and every \&quot;values[].value\&quot; are the platform&#39;s raw numbers in the stated unit. Monetary metrics also keep \&quot;values\&quot; on metricType&#x3D;total_value, because their \&quot;total\&quot; is the sum of the daily buckets the platform returned over the range: keep the series so you can reconcile that sum against the platform&#39;s own reporting before invoicing on it. A metric that could not be served is absent from this object and listed in \&quot;unavailableMetrics\&quot; instead, so an unavailable metric is never reported as a zero.  |  [optional] |
|**unavailableMetrics** | [**List&lt;InstagramAccountInsightsResponseUnavailableMetricsInner&gt;**](InstagramAccountInsightsResponseUnavailableMetricsInner.md) | Requested metrics that could not be served. Present only when at least one metric is unavailable, and absent otherwise. Each listed metric is OMITTED from \&quot;metrics\&quot; rather than reported as 0, which is how an unavailable metric is distinguished from a genuine zero. The request itself still succeeds with HTTP 200.  |  [optional] |
|**dataDelay** | **String** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| YOUTUBE | &quot;youtube&quot; |
| LINKEDIN | &quot;linkedin&quot; |
| TIKTOK | &quot;tiktok&quot; |



## Enum: MetricTypeEnum

| Name | Value |
|---- | -----|
| TIME_SERIES | &quot;time_series&quot; |
| TOTAL_VALUE | &quot;total_value&quot; |



