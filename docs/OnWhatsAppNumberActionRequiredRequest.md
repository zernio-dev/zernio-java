

# OnWhatsAppNumberActionRequiredRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**reason** | **String** |  |  [optional] |
|**requirements** | [**List&lt;OnWhatsAppNumberActionRequiredRequestRequirementsInner&gt;**](OnWhatsAppNumberActionRequiredRequestRequirementsInner.md) | Every requirement on the order with the reviewer&#39;s current verdict. Omitted when the order&#39;s requirements could not be read. |  [optional] |
|**reviewedAt** | **OffsetDateTime** | When the reviewer last commented on the order. Omitted when there is no reviewer comment. |  [optional] |
|**number** | [**OnWhatsAppNumberDeclinedRequestNumber**](OnWhatsAppNumberDeclinedRequestNumber.md) |  |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_NUMBER_ACTION_REQUIRED | &quot;whatsapp.number.action_required&quot; |



