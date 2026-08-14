

# WebhookPayloadMessageDeliveryStatus

Shared payload for message.delivered, message.read, and message.failed events. Fires when the platform reports a new delivery state for an outgoing message.  Platform support:   * message.delivered: WhatsApp, Facebook Messenger, SMS.   * message.read: WhatsApp, Facebook Messenger, Instagram. Not SMS     (carriers report delivery, never read).   * message.failed: WhatsApp and SMS (other platforms don't expose     per-message failure via webhook). On SMS, `error.code` is the     carrier's numeric code and `error.message` its reason. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**message** | [**InboxWebhookMessage**](InboxWebhookMessage.md) |  |  |
|**statusAt** | **OffsetDateTime** | When the platform reported this status. |  |
|**error** | [**WebhookPayloadMessageDeliveryStatusError**](WebhookPayloadMessageDeliveryStatusError.md) |  |  [optional] |
|**conversation** | [**InboxWebhookConversation**](InboxWebhookConversation.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| MESSAGE_DELIVERED | &quot;message.delivered&quot; |
| MESSAGE_READ | &quot;message.read&quot; |
| MESSAGE_FAILED | &quot;message.failed&quot; |



