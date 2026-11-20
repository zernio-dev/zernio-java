

# GoogleAnalyticsPlatformQueryBodyOneOf1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportType** | [**ReportTypeEnum**](#ReportTypeEnum) | A GA4 realtime report on the last 30 minutes, one page. |  |
|**accountId** | **String** | The Zernio id of the connected Google Analytics property. |  |
|**dimensions** | **List&lt;String&gt;** | GA4 dimension names, up to 9. |  [optional] |
|**metrics** | **List&lt;String&gt;** | GA4 metric names, 1 to 10. |  |
|**dimensionFilter** | **Map&lt;String, Object&gt;** | A GA4 FilterExpression on dimensions, sent to Google unchanged. |  [optional] |
|**metricFilter** | **Map&lt;String, Object&gt;** | A GA4 FilterExpression on metrics, sent to Google unchanged. |  [optional] |
|**orderBys** | **List&lt;Map&lt;String, Object&gt;&gt;** | GA4 OrderBy objects, up to 10. |  [optional] |
|**limit** | **Integer** | Rows, up to 10,000. |  [optional] |
|**minuteRanges** | [**List&lt;GoogleAnalyticsPlatformQueryBodyOneOf1MinuteRangesInner&gt;**](GoogleAnalyticsPlatformQueryBodyOneOf1MinuteRangesInner.md) | Up to 2 GA4 minute ranges. Defaults to the last 30 minutes. |  [optional] |



## Enum: ReportTypeEnum

| Name | Value |
|---- | -----|
| REALTIME | &quot;realtime&quot; |



