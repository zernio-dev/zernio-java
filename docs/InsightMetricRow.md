

# InsightMetricRow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **String** | The day with granularity&#x3D;day; fromDate with granularity&#x3D;total; null for a lifetime total. With groupBy&#x3D;demographic, the day the breakdown describes (meta.toDate). With groupBy&#x3D;keyword, the first day of the months reported (meta.fromDate). |  |
|**breakdown** | **String** | With groupBy: the segment kind, such as age, country, hour or keyword; on Search Console, the dimensions grouped, such as query,country. |  |
|**dimension** | **String** | With groupBy: the segment value, such as 25-34, US, the hour 0 to 23 as Instagram reports it, or the search keyword. Search Console: the value when one dimension is grouped, null otherwise (see dimensions). |  |
|**dimensionId** | **String** | With groupBy&#x3D;demographic on LinkedIn: the platform id of the segment. |  |
|**dimensions** | **Map&lt;String, String&gt;** | Search Console with groupBy: the value of each dimension, such as { query, country }. country is an ISO 3166-1 alpha-3 code in lowercase; device is DESKTOP, MOBILE or TABLET. |  [optional] |
|**metrics** | **Map&lt;String, BigDecimal&gt;** | Each metric asked; null when the platform did not report it for the period. |  |



