

# WebhookPayloadReferral

Webhook payload for referral received events (Instagram, Facebook Messenger)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**referral** | [**WebhookPayloadReferralReferral**](WebhookPayloadReferralReferral.md) |  |  |
|**sender** | [**WebhookPayloadReferralSender**](WebhookPayloadReferralSender.md) |  |  |
|**conversation** | [**InboxWebhookConversation**](InboxWebhookConversation.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| REFERRAL_RECEIVED | &quot;referral.received&quot; |



