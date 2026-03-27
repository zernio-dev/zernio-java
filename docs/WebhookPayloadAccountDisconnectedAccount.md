

# WebhookPayloadAccountDisconnectedAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The account&#39;s unique identifier (same as used in /v1/accounts/{accountId}) |  |
|**profileId** | **String** | The profile&#39;s unique identifier this account belongs to |  |
|**platform** | **String** |  |  |
|**username** | **String** |  |  |
|**displayName** | **String** |  |  [optional] |
|**disconnectionType** | [**DisconnectionTypeEnum**](#DisconnectionTypeEnum) | Whether the disconnection was intentional (user action) or unintentional (token expired/revoked) |  |
|**reason** | **String** | Human-readable reason for the disconnection |  |



## Enum: DisconnectionTypeEnum

| Name | Value |
|---- | -----|
| INTENTIONAL | &quot;intentional&quot; |
| UNINTENTIONAL | &quot;unintentional&quot; |



