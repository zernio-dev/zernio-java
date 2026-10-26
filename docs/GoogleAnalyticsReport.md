

# GoogleAnalyticsReport

Google Analytics Data API report, passed through as Google returns it. Every value in `rows` is a string; read `metricHeaders[].type` to parse metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio account ID of the Google Analytics connection. |  [optional] |
|**propertyId** | **String** | Numeric GA4 property ID. |  [optional] |
|**dimensionHeaders** | [**List&lt;GoogleAnalyticsReportDimensionHeadersInner&gt;**](GoogleAnalyticsReportDimensionHeadersInner.md) |  |  [optional] |
|**metricHeaders** | [**List&lt;GoogleAnalyticsReportMetricHeadersInner&gt;**](GoogleAnalyticsReportMetricHeadersInner.md) |  |  [optional] |
|**rows** | [**List&lt;GoogleAnalyticsReportRowsInner&gt;**](GoogleAnalyticsReportRowsInner.md) |  |  [optional] |
|**rowCount** | **Integer** | Total rows matching the request, across all pages. |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | Google report metadata (currency, time zone, sampling and thresholding flags). |  [optional] |
|**propertyQuota** | **Map&lt;String, Object&gt;** | Google quota left on this property after the request (tokens per day and per hour, concurrent requests). Cached responses carry the quota from when they were fetched. |  [optional] |



