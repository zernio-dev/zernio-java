

# WebhookPayloadWhatsAppAccountStatusUpdated

Webhook payload for `whatsapp.account.status_updated`. Fired when Meta restricts, flags a violation on, disables, deletes or reinstates the WhatsApp Business Account. The same status is also exposed on the account as `platformStatus`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadWhatsAppAccountQualityUpdatedAccount**](WebhookPayloadWhatsAppAccountQualityUpdatedAccount.md) |  |  |
|**status** | [**WebhookPayloadWhatsAppAccountStatusUpdatedStatus**](WebhookPayloadWhatsAppAccountStatusUpdatedStatus.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_ACCOUNT_STATUS_UPDATED | &quot;whatsapp.account.status_updated&quot; |



