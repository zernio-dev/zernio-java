

# WebhookPayloadWhatsAppAccountQualityUpdated

Webhook payload for `whatsapp.account.quality_updated`. Fired when a connected number's quality rating or messaging limit tier differs from the value Zernio held. Tier changes that Meta applies to the whole portfolio fire once per connected number. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadWhatsAppAccountQualityUpdatedAccount**](WebhookPayloadWhatsAppAccountQualityUpdatedAccount.md) |  |  |
|**quality** | [**WebhookPayloadWhatsAppAccountQualityUpdatedQuality**](WebhookPayloadWhatsAppAccountQualityUpdatedQuality.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_ACCOUNT_QUALITY_UPDATED | &quot;whatsapp.account.quality_updated&quot; |



