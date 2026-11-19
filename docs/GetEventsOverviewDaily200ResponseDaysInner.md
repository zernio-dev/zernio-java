

# GetEventsOverviewDaily200ResponseDaysInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**day** | **LocalDate** |  |  [optional] |
|**conversions** | **Integer** | Stored events that occurred that day. |  [optional] |
|**sent** | **Integer** | Events first sent to a destination that day. |  [optional] |
|**accepted** | **Integer** | Those the platform accepted. |  [optional] |
|**value** | **BigDecimal** | The day&#39;s value, in the period&#39;s &#x60;totals.currency&#x60;. |  [optional] |
|**valueSent** | **BigDecimal** | Of that value, the conversions a platform accepted. |  [optional] |
|**fromAds** | **Integer** | Counted events that came from an ad, as in &#x60;totals.fromAds&#x60;. |  [optional] |
|**matched** | **Integer** | Events matched to an ad campaign. |  [optional] |
|**byEvent** | **Map&lt;String, Integer&gt;** | The day&#39;s stored events per event name. |  [optional] |



