

# WebhookPayloadCallFailed

Webhook payload for the `call.failed` event. Fired when a call setup or in-progress call fails. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**call** | [**WebhookPayloadCallFailedCall**](WebhookPayloadCallFailedCall.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CALL_FAILED | &quot;call.failed&quot; |



