

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
|**analyticsSync** | [**GetAllAccountsHealth200ResponseAccountsInnerAnalyticsSync**](GetAllAccountsHealth200ResponseAccountsInnerAnalyticsSync.md) |  |  [optional] |
|**messagingRestriction** | [**GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction**](GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction.md) |  |  [optional] |
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



