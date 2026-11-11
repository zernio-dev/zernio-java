

# GetEventsOverview200ResponseToday


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversions** | **Integer** | Stored events that occurred today, retracted ones excluded. |  [optional] |
|**value** | **BigDecimal** | Value of those events in &#x60;currency&#x60;. Events in other currencies are left out. |  [optional] |
|**currency** | **String** | The currency most of today&#39;s valued events use; &#x60;null&#x60; when none carried a value. |  [optional] |
|**sent** | **Integer** | Event sends to a destination today, one per event and destination. |  [optional] |
|**accepted** | **Integer** | Those whose latest send the platform accepted. |  [optional] |
|**matched** | **Integer** | Today&#39;s events matched to an ad campaign. |  [optional] |



