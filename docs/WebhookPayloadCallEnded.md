

# WebhookPayloadCallEnded

Webhook payload for the `call.ended` event. Fires on call hangup with the duration and a zero-markup billing breakdown. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**call** | [**WebhookPayloadCallEndedCall**](WebhookPayloadCallEndedCall.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CALL_ENDED | &quot;call.ended&quot; |



