

# WebhookPayloadCallReceived

Webhook payload for the `call.received` event. Fires for both inbound (UIC) and outbound (BIC) calls; branch on `call.direction` to tell them apart. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**call** | [**WebhookPayloadCallReceivedCall**](WebhookPayloadCallReceivedCall.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CALL_RECEIVED | &quot;call.received&quot; |



