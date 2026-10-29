

# GetAccountHealth200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**integrationLane** | [**IntegrationLaneEnum**](#IntegrationLaneEnum) | TikTok only. The TikTok integration the account is connected through: business (TikTok for Business, Accounts API) or developer (the original integration). Absent on other platforms. |  [optional] |
|**sendCap** | [**GetAccountHealth200ResponseSendCap**](GetAccountHealth200ResponseSendCap.md) |  |  [optional] |
|**push** | [**PushEnum**](#PushEnum) | Google and Microsoft only: state of the provider change-notification subscriptions behind &#x60;message.received&#x60; and &#x60;calendar.event.*&#x60;. &#x60;pending&#x60; means a granted area has no live subscription yet (retried every 6 hours), &#x60;failed&#x60; that renewals keep failing (reconnect the account). |  [optional] |
|**username** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Overall health status |  [optional] |
|**tokenStatus** | [**GetAccountHealth200ResponseTokenStatus**](GetAccountHealth200ResponseTokenStatus.md) |  |  [optional] |
|**permissions** | [**GetAccountHealth200ResponsePermissions**](GetAccountHealth200ResponsePermissions.md) |  |  [optional] |
|**issues** | **List&lt;String&gt;** | List of issues found |  [optional] |
|**recommendations** | **List&lt;String&gt;** | Actionable recommendations to fix issues |  [optional] |
|**ownerUserId** | **String** | User id of the profile owner, not necessarily the team member who connected the account. |  [optional] |
|**disconnectReason** | **String** | Why the connection is broken or its token refresh is failing, from the most recent current cause. Null when the connection is healthy, including when the account is unhealthy for another reason (analytics, messaging restriction, missing analytics scopes), or when no cause is stored. |  [optional] |
|**disconnectionType** | [**DisconnectionTypeEnum**](#DisconnectionTypeEnum) | intentional: deliberately disconnected by the user or by Zernio (for example a plan downgrade), not a token failure. unintentional: token expired or revoked, or an auth failure. Null when disconnectReason is null. |  [optional] |
|**unhealthySince** | **OffsetDateTime** | When the earliest current stored cause was recorded (the start of the outage); for an intentional disconnect, when it was disconnected. Null when the connection is healthy, including when the account is unhealthy for another reason (analytics, messaging restriction, missing analytics scopes), or when the time is unknown. |  [optional] |
|**analyticsSync** | [**GetAllAccountsHealth200ResponseAccountsInnerAnalyticsSync**](GetAllAccountsHealth200ResponseAccountsInnerAnalyticsSync.md) |  |  [optional] |
|**messagingRestriction** | [**GetAccountHealth200ResponseMessagingRestriction**](GetAccountHealth200ResponseMessagingRestriction.md) |  |  [optional] |
|**platformConnection** | [**GetAccountHealth200ResponsePlatformConnection**](GetAccountHealth200ResponsePlatformConnection.md) |  |  [optional] |



## Enum: IntegrationLaneEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| DEVELOPER | &quot;developer&quot; |



## Enum: PushEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PENDING | &quot;pending&quot; |
| FAILED | &quot;failed&quot; |
| NOT_APPLICABLE | &quot;not_applicable&quot; |



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



