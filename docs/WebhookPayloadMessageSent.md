

# WebhookPayloadMessageSent

Webhook payload for message sent events (fired when a message is sent via the API, or from the WhatsApp Business app on Coexistence numbers)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**message** | [**WebhookPayloadMessageSentMessage**](WebhookPayloadMessageSentMessage.md) |  |  |
|**pricing** | [**WhatsAppMessagePricing**](WhatsAppMessagePricing.md) |  |  [optional] |
|**billingConversation** | [**WhatsAppBillingConversation**](WhatsAppBillingConversation.md) |  |  [optional] |
|**conversation** | [**InboxWebhookConversation**](InboxWebhookConversation.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**metadata** | [**WebhookPayloadMessageSentMetadata**](WebhookPayloadMessageSentMetadata.md) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| MESSAGE_SENT | &quot;message.sent&quot; |



