

# WebhookPayloadConversationControlChanged

WhatsApp only. Who answers a conversation changed: Meta Business Agent took it over, handed it to you, or another partner app took it. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**conversation** | [**InboxWebhookConversationDetail**](InboxWebhookConversationDetail.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**control** | [**WebhookPayloadConversationControlChangedControl**](WebhookPayloadConversationControlChangedControl.md) |  |  |
|**changedAt** | **OffsetDateTime** |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CONVERSATION_CONTROL_CHANGED | &quot;conversation.control_changed&quot; |



