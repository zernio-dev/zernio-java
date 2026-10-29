

# WebhookPayloadMessageDeliveryStatus

Shared payload for message.delivered, message.read, message.played and message.failed events. Fires when the platform reports a new delivery state for an outgoing message.  **Platform support:**  - message.delivered: WhatsApp, Facebook Messenger, SMS, RCS. - message.read: WhatsApp, Facebook Messenger, Instagram, RCS. Not SMS (carriers report delivery, never read). - message.played: WhatsApp only, voice messages. - message.failed: WhatsApp, SMS and RCS (other platforms don't expose per-message failure via webhook). On SMS, `error.code` is the carrier's numeric code and `error.message` its reason. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**message** | [**InboxWebhookMessage**](InboxWebhookMessage.md) |  |  |
|**statusAt** | **OffsetDateTime** | When the platform reported this status. |  |
|**error** | [**WebhookPayloadMessageDeliveryStatusError**](WebhookPayloadMessageDeliveryStatusError.md) |  |  [optional] |
|**pricing** | [**WhatsAppMessagePricing**](WhatsAppMessagePricing.md) |  |  [optional] |
|**billingConversation** | [**WhatsAppBillingConversation**](WhatsAppBillingConversation.md) |  |  [optional] |
|**conversation** | [**InboxWebhookConversation**](InboxWebhookConversation.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| MESSAGE_DELIVERED | &quot;message.delivered&quot; |
| MESSAGE_READ | &quot;message.read&quot; |
| MESSAGE_PLAYED | &quot;message.played&quot; |
| MESSAGE_FAILED | &quot;message.failed&quot; |



