

# GetAllAccountsHealth200ResponseAccountsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**canPost** | **Boolean** |  |  [optional] |
|**canFetchAnalytics** | **Boolean** |  |  [optional] |
|**tokenValid** | **Boolean** |  |  [optional] |
|**tokenExpiresAt** | **OffsetDateTime** |  |  [optional] |
|**needsReconnect** | **Boolean** | True when the token is expired or revoked, permissions are missing, the account is inactive, or the platform rejected its stored credentials (the same flag the account listing reports as needsReconnection). |  [optional] |
|**issues** | **List&lt;String&gt;** |  |  [optional] |
|**messagingRestriction** | [**GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction**](GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| HEALTHY | &quot;healthy&quot; |
| WARNING | &quot;warning&quot; |
| ERROR | &quot;error&quot; |



