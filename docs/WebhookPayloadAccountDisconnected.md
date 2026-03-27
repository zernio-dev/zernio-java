

# WebhookPayloadAccountDisconnected

Webhook payload for account disconnected events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadAccountDisconnectedAccount**](WebhookPayloadAccountDisconnectedAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| ACCOUNT_DISCONNECTED | &quot;account.disconnected&quot; |



