

# OnWhatsAppAutomaticEventRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** |  |  [optional] |
|**accountId** | **String** | SocialAccount id of the WhatsApp number whose conversation was flagged. |  [optional] |
|**conversationId** | **String** | Zernio conversation id, when the thread could be resolved. |  [optional] |
|**platformMessageId** | **String** | The wamid of the message Meta&#39;s analysis flagged. |  [optional] |
|**eventName** | **String** | Meta-detected event: &#x60;LeadSubmitted&#x60; | &#x60;Purchase&#x60;. |  [optional] |
|**ctwaClid** | **String** | Meta&#39;s CTWA click id, the Conversions API match key. |  [optional] |
|**customData** | [**OnWhatsAppAutomaticEventRequestCustomData**](OnWhatsAppAutomaticEventRequestCustomData.md) |  |  [optional] |
|**detectedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_AUTOMATIC_EVENT | &quot;whatsapp.automatic_event&quot; |



