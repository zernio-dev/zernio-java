

# WebhookPayloadWhatsAppAccountNameStatusUpdated

Webhook payload for the `whatsapp.account.name_status_updated` event. Fired when Meta finishes reviewing a WhatsApp display-name change on a connected number. Maps Meta's `phone_number_name_update` WABA webhook field onto our event envelope. Fires only for a review outcome (APPROVED, DECLINED, PENDING_REVIEW); a name applied without review reports `name_status: AVAILABLE_WITHOUT_REVIEW` on the phone node instead, and Meta never sends this webhook field for that case. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadWhatsAppTemplateStatusUpdatedAccount**](WebhookPayloadWhatsAppTemplateStatusUpdatedAccount.md) |  |  |
|**name** | [**WebhookPayloadWhatsAppAccountNameStatusUpdatedName**](WebhookPayloadWhatsAppAccountNameStatusUpdatedName.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_ACCOUNT_NAME_STATUS_UPDATED | &quot;whatsapp.account.name_status_updated&quot; |



