

# RunGoogleAnalyticsReportRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio account ID of the Google Analytics connection (platform &#x60;googleanalytics&#x60;). |  |
|**dimensions** | **List&lt;String&gt;** | GA4 dimension API names, e.g. &#x60;date&#x60;, &#x60;sessionSource&#x60;, &#x60;pagePath&#x60;. List them with GET /v1/analytics/googleanalytics/metadata. |  [optional] |
|**metrics** | **List&lt;String&gt;** | GA4 metric API names, e.g. &#x60;sessions&#x60;, &#x60;activeUsers&#x60;, &#x60;keyEvents&#x60;, &#x60;totalRevenue&#x60;. |  |
|**dimensionFilter** | **Map&lt;String, Object&gt;** | A Google FilterExpression on dimensions, in Google&#39;s own shape. |  [optional] |
|**metricFilter** | **Map&lt;String, Object&gt;** | A Google FilterExpression on metrics, in Google&#39;s own shape. |  [optional] |
|**orderBys** | **List&lt;Map&lt;String, Object&gt;&gt;** | Google OrderBy objects, e.g. &#x60;{ \&quot;metric\&quot;: { \&quot;metricName\&quot;: \&quot;sessions\&quot; }, \&quot;desc\&quot;: true }&#x60;. |  [optional] |
|**limit** | **Integer** | Rows to return. Defaults to Google&#39;s default (10000). |  [optional] |
|**dateRanges** | [**List&lt;RunGoogleAnalyticsReportRequestAllOfDateRangesInner&gt;**](RunGoogleAnalyticsReportRequestAllOfDateRangesInner.md) | Defaults to the last 28 days (&#x60;28daysAgo&#x60; to &#x60;yesterday&#x60;). |  [optional] |
|**offset** | **Integer** | Row offset for paging through a report larger than &#x60;limit&#x60;. |  [optional] |
|**keepEmptyRows** | **Boolean** |  |  [optional] |
|**currencyCode** | **String** | ISO 4217 code for currency metrics. Defaults to the property currency. |  [optional] |



