

# AdMetricRow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **String** |  |  |
|**name** | **String** |  |  |
|**platform** | **String** |  |  |
|**status** | **String** |  |  |
|**currency** | **String** |  |  |
|**summary** | [**AdMetricRowSummary**](AdMetricRowSummary.md) |  |  |
|**daily** | [**List&lt;AdMetricRowDailyInner&gt;**](AdMetricRowDailyInner.md) | With granularity&#x3D;day: one point per day. |  [optional] |
|**breakdowns** | **Map&lt;String, Object&gt;** | With breakdowns: read live from the platform. |  [optional] |
|**unsupportedBreakdowns** | **List&lt;String&gt;** |  |  [optional] |
|**breakdownHints** | **Map&lt;String, String&gt;** |  |  [optional] |
|**breakdownsRange** | **Object** |  |  [optional] |
|**breakdownErrors** | **List&lt;Object&gt;** |  |  [optional] |
|**breakdownDroppedMetrics** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |



