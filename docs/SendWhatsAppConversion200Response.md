

# SendWhatsAppConversion200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**eventsReceived** | **Integer** | Events accepted by Meta. |  [optional] |
|**eventsFailed** | **Integer** | Events rejected by Meta (see failures). |  [optional] |
|**failures** | [**List&lt;SendWhatsAppConversion200ResponseFailuresInner&gt;**](SendWhatsAppConversion200ResponseFailuresInner.md) | Per-event failure detail. Empty when all events were accepted.  |  [optional] |
|**traceId** | **String** | Meta &#x60;fbtrace_id&#x60; for debugging. Surface in support tickets.  |  [optional] |
|**platformMessages** | **List&lt;String&gt;** | Meta&#39;s &#x60;messages&#x60; (warnings about the events it accepted), each distinct one once, at most 20. Absent when Meta sent none. |  [optional] |
|**testCode** | **String** | The test code sent to Meta, or &#x60;null&#x60; when the request carried none. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| METAADS | &quot;metaads&quot; |



