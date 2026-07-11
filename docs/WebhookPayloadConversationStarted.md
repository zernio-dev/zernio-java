

# WebhookPayloadConversationStarted

Fired once when a new conversation begins, in either direction. A conversation starts the first time an account and a contact exchange a message on any DM platform (Instagram, Messenger/Facebook, Telegram, WhatsApp, Twitter, Reddit, Bluesky, SMS). Platform-agnostic — one subscription covers every DM platform. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**conversation** | [**WebhookPayloadConversationStartedConversation**](WebhookPayloadConversationStartedConversation.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**startedAt** | **OffsetDateTime** | When the conversation document was created. |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CONVERSATION_STARTED | &quot;conversation.started&quot; |



