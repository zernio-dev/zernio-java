

# ListWhatsAppConversions200ResponseEventsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**timestamp** | **OffsetDateTime** | When the event was sent to Meta. |  [optional] |
|**eventName** | **String** | One of LeadSubmitted, Purchase, AddToCart, InitiateCheckout, ViewContent. |  [optional] |
|**conversationId** | **String** |  |  [optional] |
|**eventsReceived** | **Integer** | Number of events Meta accepted on this send (usually 1). |  [optional] |
|**eventsFailed** | **Integer** | Number of events Meta rejected (usually 0). |  [optional] |
|**traceId** | **String** | Meta fbtrace_id for cross-referencing in Events Manager. |  [optional] |
|**durationMs** | **Integer** |  |  [optional] |



