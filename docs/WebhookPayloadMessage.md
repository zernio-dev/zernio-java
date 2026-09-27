

# WebhookPayloadMessage

Webhook payload for message received events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**message** | [**WebhookPayloadMessageMessage**](WebhookPayloadMessageMessage.md) |  |  |
|**conversation** | [**InboxWebhookConversation**](InboxWebhookConversation.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**metadata** | [**WebhookPayloadMessageMetadata**](WebhookPayloadMessageMetadata.md) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| MESSAGE_RECEIVED | &quot;message.received&quot; |



