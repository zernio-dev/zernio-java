

# WebhookPayloadMessage

Webhook payload for message received events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**message** | [**WebhookPayloadMessageMessage**](WebhookPayloadMessageMessage.md) |  |  |
|**conversation** | [**WebhookPayloadReactionConversation**](WebhookPayloadReactionConversation.md) |  |  |
|**account** | [**WebhookPayloadReactionAccount**](WebhookPayloadReactionAccount.md) |  |  |
|**metadata** | [**WebhookPayloadMessageMetadata**](WebhookPayloadMessageMetadata.md) |  |  [optional] |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| MESSAGE_RECEIVED | &quot;message.received&quot; |



