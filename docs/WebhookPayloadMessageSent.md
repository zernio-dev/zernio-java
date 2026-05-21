

# WebhookPayloadMessageSent

Webhook payload for message sent events (fired when a message is sent via the API)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**message** | [**WebhookPayloadMessageSentMessage**](WebhookPayloadMessageSentMessage.md) |  |  |
|**conversation** | [**WebhookPayloadReactionConversation**](WebhookPayloadReactionConversation.md) |  |  |
|**account** | [**WebhookPayloadReactionAccount**](WebhookPayloadReactionAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| MESSAGE_SENT | &quot;message.sent&quot; |



