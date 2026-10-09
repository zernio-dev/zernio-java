

# WebhookPayloadConversationControlChanged

Who answers a conversation changed under Meta's handover protocol. WhatsApp: Meta Business Agent took it over, handed it to you, or another partner app took it. Facebook and Instagram: another app passed the thread to you, or took or received it. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
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



