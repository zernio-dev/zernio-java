

# WebhookPayloadCallReceived

Webhook payload for the `call.received` event. Fires for both inbound (UIC) and outbound (BIC) calls; branch on `call.direction` to tell them apart. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**call** | [**WebhookPayloadCallReceivedCall**](WebhookPayloadCallReceivedCall.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CALL_RECEIVED | &quot;call.received&quot; |



