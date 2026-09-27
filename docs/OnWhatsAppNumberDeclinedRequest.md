

# OnWhatsAppNumberDeclinedRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**number** | [**OnWhatsAppNumberDeclinedRequestNumber**](OnWhatsAppNumberDeclinedRequestNumber.md) |  |  [optional] |
|**reason** | **String** |  |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_NUMBER_DECLINED | &quot;whatsapp.number.declined&quot; |



