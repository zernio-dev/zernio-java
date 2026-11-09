

# SendEventsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Profile the events belong to. Its saved destinations receive the events. |  |
|**events** | [**List&lt;ConversionEvent&gt;**](ConversionEvent.md) |  |  |
|**destinations** | [**List&lt;SendEventsRequestDestinationsInner&gt;**](SendEventsRequestDestinationsInner.md) | Send to these destinations instead of the saved ones (every event goes to each). |  [optional] |
|**consent** | [**SendEventsRequestConsent**](SendEventsRequestConsent.md) |  |  [optional] |
|**testCode** | **String** | Forwarded as each platform test code (see POST /v1/ads/conversions). A root-level &#x60;test_event_code&#x60; is accepted as an alias. Test events are not stored. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | &#x60;sync&#x60; sends to every destination before answering (200, per-destination results). &#x60;async&#x60; stores and queues the sends, then answers 202 at once; each send is retried while the platform fails for now, and its outcome shows on GET /v1/events/{eventId}. Requests with &#x60;testCode&#x60; always send now. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| SYNC | &quot;sync&quot; |
| ASYNC | &quot;async&quot; |



