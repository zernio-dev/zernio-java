

# GoogleAnalyticsPlatformQueryBodyOneOf


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportType** | [**ReportTypeEnum**](#ReportTypeEnum) | A GA4 report over date ranges, paged with a cursor. |  |
|**accountId** | **String** | The Zernio id of the connected Google Analytics property. |  |
|**dimensions** | **List&lt;String&gt;** | GA4 dimension names, up to 9. |  [optional] |
|**metrics** | **List&lt;String&gt;** | GA4 metric names, 1 to 10. |  |
|**dimensionFilter** | **Map&lt;String, Object&gt;** | A GA4 FilterExpression on dimensions, sent to Google unchanged. |  [optional] |
|**metricFilter** | **Map&lt;String, Object&gt;** | A GA4 FilterExpression on metrics, sent to Google unchanged. |  [optional] |
|**orderBys** | **List&lt;Map&lt;String, Object&gt;&gt;** | GA4 OrderBy objects, up to 10. |  [optional] |
|**limit** | **Integer** | Rows per page, up to 10,000. Defaults to 10,000. |  [optional] |
|**dateRanges** | [**List&lt;GoogleAnalyticsPlatformQueryBodyOneOfDateRangesInner&gt;**](GoogleAnalyticsPlatformQueryBodyOneOfDateRangesInner.md) | Up to 4 GA4 date ranges. Defaults to the 28 days ending yesterday. |  [optional] |
|**keepEmptyRows** | **Boolean** | Keep rows whose metrics are all 0. |  [optional] |
|**currencyCode** | **String** | ISO 4217 code for money metrics. |  [optional] |
|**cursor** | **String** | The pagination.nextCursor of the previous page, unchanged. |  [optional] |



## Enum: ReportTypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |



