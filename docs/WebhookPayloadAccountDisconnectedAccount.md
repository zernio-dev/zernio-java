

# WebhookPayloadAccountDisconnectedAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The account&#39;s unique identifier (same as used in /v1/accounts/{accountId}) |  |
|**profileId** | **String** | The profile&#39;s unique identifier this account belongs to |  |
|**platform** | **String** |  |  |
|**username** | **String** |  |  |
|**displayName** | **String** |  |  [optional] |
|**disconnectionType** | [**DisconnectionTypeEnum**](#DisconnectionTypeEnum) | intentional: removed on purpose, for example with DELETE /v1/accounts/{accountId} or by a switch to the Free plan for the accounts over its limit. The account is deleted permanently 1 hour later unless the same account is reconnected within that hour.  unintentional: the connection broke (token expired or revoked, access lost on the platform). The account stays in Zernio, inactive, until it is reconnected (keeping its accountId) or removed. |  |
|**reason** | **String** | Human-readable reason for the disconnection |  |



## Enum: DisconnectionTypeEnum

| Name | Value |
|---- | -----|
| INTENTIONAL | &quot;intentional&quot; |
| UNINTENTIONAL | &quot;unintentional&quot; |



