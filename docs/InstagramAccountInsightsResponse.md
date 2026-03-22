

# InstagramAccountInsightsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**accountId** | **String** | The Zernio SocialAccount ID |  [optional] |
|**platform** | **String** |  |  [optional] |
|**dateRange** | [**InstagramAccountInsightsResponseDateRange**](InstagramAccountInsightsResponseDateRange.md) |  |  [optional] |
|**metricType** | [**MetricTypeEnum**](#MetricTypeEnum) |  |  [optional] |
|**breakdown** | **String** | Breakdown dimension used (only present when breakdown was requested) |  [optional] |
|**metrics** | [**Map&lt;String, InstagramAccountInsightsResponseMetricsValue&gt;**](InstagramAccountInsightsResponseMetricsValue.md) | Object keyed by metric name. For time_series: each metric has \&quot;total\&quot; (number) and \&quot;values\&quot; (array of {date, value}). For total_value: each metric has \&quot;total\&quot; (number) and optionally \&quot;breakdowns\&quot; (array of {dimension, value}).  |  [optional] |
|**dataDelay** | **String** |  |  [optional] |



## Enum: MetricTypeEnum

| Name | Value |
|---- | -----|
| TIME_SERIES | &quot;time_series&quot; |
| TOTAL_VALUE | &quot;total_value&quot; |



