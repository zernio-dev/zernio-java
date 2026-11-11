

# GetEventsOverview200ResponsePlatformsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** | Ad platform, such as &#x60;metaads&#x60; or &#x60;googleads&#x60;. |  [optional] |
|**accountName** | **String** |  |  [optional] |
|**destinationName** | **String** | The destination (pixel, dataset or conversion action) id. |  [optional] |
|**sentToday** | **Integer** | Events the platform accepted today. |  [optional] |
|**failedToday** | **Integer** | Events that failed for good today. |  [optional] |
|**lastSentAt** | **OffsetDateTime** | Last accepted send in the last 30 days. |  [optional] |
|**lastEventName** | **String** | Name of the event in that send. |  [optional] |
|**lastError** | **String** | The platform&#39;s error on the last failed send in the last 30 days. |  [optional] |
|**fixUrl** | **String** | Where to fix a failing destination. Always &#x60;null&#x60; for now. |  [optional] |



