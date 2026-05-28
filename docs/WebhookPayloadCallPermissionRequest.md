

# WebhookPayloadCallPermissionRequest

Webhook payload for the `call.permission_request` event. Fires when a consumer accepts or rejects an interactive `call_permission_request` message. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**permission** | [**WebhookPayloadCallPermissionRequestPermission**](WebhookPayloadCallPermissionRequestPermission.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CALL_PERMISSION_REQUEST | &quot;call.permission_request&quot; |



