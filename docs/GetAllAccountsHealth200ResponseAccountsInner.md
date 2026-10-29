

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
|**ownerUserId** | **String** | User id of the profile owner, not necessarily the team member who connected the account. |  [optional] |
|**disconnectReason** | **String** | Why the connection is broken or its token refresh is failing, from the most recent current cause. Null when the connection is healthy, including when the account is unhealthy for another reason (analytics, messaging restriction, missing analytics scopes), or when no cause is stored. |  [optional] |
|**disconnectionType** | [**DisconnectionTypeEnum**](#DisconnectionTypeEnum) | intentional: deliberately disconnected by the user or by Zernio (for example a plan downgrade), not a token failure. unintentional: token expired or revoked, or an auth failure. Null when disconnectReason is null. |  [optional] |
|**unhealthySince** | **OffsetDateTime** | When the earliest current stored cause was recorded (the start of the outage); for an intentional disconnect, when it was disconnected. Null when the connection is healthy, including when the account is unhealthy for another reason (analytics, messaging restriction, missing analytics scopes), or when the time is unknown. |  [optional] |
|**analyticsSync** | [**GetAllAccountsHealth200ResponseAccountsInnerAnalyticsSync**](GetAllAccountsHealth200ResponseAccountsInnerAnalyticsSync.md) |  |  [optional] |
|**messagingRestriction** | [**GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction**](GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| HEALTHY | &quot;healthy&quot; |
| WARNING | &quot;warning&quot; |
| ERROR | &quot;error&quot; |



## Enum: DisconnectionTypeEnum

| Name | Value |
|---- | -----|
| INTENTIONAL | &quot;intentional&quot; |
| UNINTENTIONAL | &quot;unintentional&quot; |



