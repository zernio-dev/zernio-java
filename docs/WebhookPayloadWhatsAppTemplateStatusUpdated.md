

# WebhookPayloadWhatsAppTemplateStatusUpdated

Webhook payload for the `whatsapp.template.status_updated` event. Fired when Meta completes (re)review of a template attached to a connected WABA. Maps Meta's `message_template_status_update` field onto our event envelope. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadWhatsAppTemplateStatusUpdatedAccount**](WebhookPayloadWhatsAppTemplateStatusUpdatedAccount.md) |  |  |
|**template** | [**WebhookPayloadWhatsAppTemplateStatusUpdatedTemplate**](WebhookPayloadWhatsAppTemplateStatusUpdatedTemplate.md) |  |  |
|**timestamp** | **OffsetDateTime** | ISO-8601 timestamp the webhook was produced. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_TEMPLATE_STATUS_UPDATED | &quot;whatsapp.template.status_updated&quot; |



