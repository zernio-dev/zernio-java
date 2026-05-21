

# WebhookPayloadReaction

Webhook payload for reaction received events (WhatsApp, Telegram)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**reaction** | [**WebhookPayloadReactionReaction**](WebhookPayloadReactionReaction.md) |  |  |
|**conversation** | [**WebhookPayloadReactionConversation**](WebhookPayloadReactionConversation.md) |  |  |
|**account** | [**WebhookPayloadReactionAccount**](WebhookPayloadReactionAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| REACTION_RECEIVED | &quot;reaction.received&quot; |



