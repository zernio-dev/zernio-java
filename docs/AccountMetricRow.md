

# AccountMetricRow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **String** | Start of the period: the day, the Monday of the week or the first of the month, never before fromDate. With granularity&#x3D;total, fromDate. |  |
|**accountId** | **String** | With groupBy&#x3D;account. |  |
|**platform** | **String** | With groupBy&#x3D;account or groupBy&#x3D;platform. |  |
|**profileId** | **String** | With groupBy&#x3D;account. |  |
|**username** | **String** | With groupBy&#x3D;account. |  |
|**metrics** | **Map&lt;String, BigDecimal&gt;** | Each metric asked; null when no account in the row reports it or no follower snapshot exists in the period. |  |



