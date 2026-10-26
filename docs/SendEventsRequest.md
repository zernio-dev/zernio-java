

# SendEventsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Profile the events belong to. Its saved destinations receive the events. |  |
|**events** | [**List&lt;ConversionEvent&gt;**](ConversionEvent.md) |  |  |
|**destinations** | [**List&lt;SendEventsRequestDestinationsInner&gt;**](SendEventsRequestDestinationsInner.md) | Send to these destinations instead of the saved ones (every event goes to each). |  [optional] |
|**consent** | [**SendEventsRequestConsent**](SendEventsRequestConsent.md) |  |  [optional] |
|**testCode** | **String** | Forwarded as each platform test code (see POST /v1/ads/conversions). Test events are not stored. |  [optional] |



