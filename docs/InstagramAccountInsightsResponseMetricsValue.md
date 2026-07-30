

# InstagramAccountInsightsResponseMetricsValue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**total** | **BigDecimal** | Sum or aggregate value for the metric |  [optional] |
|**values** | [**List&lt;InstagramAccountInsightsResponseMetricsValueValuesInner&gt;**](InstagramAccountInsightsResponseMetricsValueValuesInner.md) | Daily values (for time_series, and always on monetary metrics) |  [optional] |
|**breakdowns** | [**List&lt;InstagramAccountInsightsResponseMetricsValueBreakdownsInner&gt;**](InstagramAccountInsightsResponseMetricsValueBreakdownsInner.md) | Breakdown values (only for total_value with breakdown) |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | Present on monetary metrics only. The scale of \&quot;total\&quot; and of every \&quot;values[].value\&quot;, exactly as the platform returned them.  \&quot;micro_amount\&quot;: the platform returned an object shape carrying a micro amount, and the values are that integer, summed, unconverted. Zernio does not publish a divisor because Meta does not document one; divide by the scale you have verified against the Page&#39;s own Meta Business Suite export. On Facebook Page insights this is always content_monetization_earnings.  \&quot;unspecified\&quot;: the platform returned a bare number with no unit metadata. It is passed through as-is; the platform does not state whether it is major or minor currency units. On Facebook Page insights this is always monetization_approximate_earnings.  |  [optional] |
|**currency** | **String** | ISO 4217 currency of a monetary metric, or null when the platform omitted it. Always null on monetization_approximate_earnings, which Meta returns as a bare number with no currency; always present on content_monetization_earnings.  |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| MICRO_AMOUNT | &quot;micro_amount&quot; |
| UNSPECIFIED | &quot;unspecified&quot; |



