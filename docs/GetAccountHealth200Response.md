

# GetAccountHealth200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**integrationLane** | [**IntegrationLaneEnum**](#IntegrationLaneEnum) | TikTok only. The TikTok integration the account is connected through: business (TikTok for Business, Accounts API) or developer (the original integration). Absent on other platforms. |  [optional] |
|**username** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Overall health status |  [optional] |
|**tokenStatus** | [**GetAccountHealth200ResponseTokenStatus**](GetAccountHealth200ResponseTokenStatus.md) |  |  [optional] |
|**permissions** | [**GetAccountHealth200ResponsePermissions**](GetAccountHealth200ResponsePermissions.md) |  |  [optional] |
|**issues** | **List&lt;String&gt;** | List of issues found |  [optional] |
|**recommendations** | **List&lt;String&gt;** | Actionable recommendations to fix issues |  [optional] |
|**messagingRestriction** | [**GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction**](GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction.md) |  |  [optional] |
|**platformConnection** | [**GetAccountHealth200ResponsePlatformConnection**](GetAccountHealth200ResponsePlatformConnection.md) |  |  [optional] |



## Enum: IntegrationLaneEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| DEVELOPER | &quot;developer&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| HEALTHY | &quot;healthy&quot; |
| WARNING | &quot;warning&quot; |
| ERROR | &quot;error&quot; |



