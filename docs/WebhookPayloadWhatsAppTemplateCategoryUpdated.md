

# WebhookPayloadWhatsAppTemplateCategoryUpdated

Webhook payload for the `whatsapp.template.category_updated` event. Fired when Meta reclassifies a template's category attached to a connected WABA. Maps Meta's `template_category_update` field onto our event envelope. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadWhatsAppTemplateStatusUpdatedAccount**](WebhookPayloadWhatsAppTemplateStatusUpdatedAccount.md) |  |  |
|**template** | [**WebhookPayloadWhatsAppTemplateCategoryUpdatedTemplate**](WebhookPayloadWhatsAppTemplateCategoryUpdatedTemplate.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_TEMPLATE_CATEGORY_UPDATED | &quot;whatsapp.template.category_updated&quot; |



