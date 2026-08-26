

# WebhookPayloadMessageSent

Webhook payload for message sent events (fired when a message is sent via the API, or from the WhatsApp Business app on Coexistence numbers)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**message** | [**WebhookPayloadMessageSentMessage**](WebhookPayloadMessageSentMessage.md) |  |  |
|**conversation** | [**InboxWebhookConversation**](InboxWebhookConversation.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**metadata** | [**WebhookPayloadMessageSentMetadata**](WebhookPayloadMessageSentMetadata.md) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| MESSAGE_SENT | &quot;message.sent&quot; |



