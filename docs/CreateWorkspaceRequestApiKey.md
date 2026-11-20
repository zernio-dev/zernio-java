

# CreateWorkspaceRequestApiKey

Mint a key that acts in the new workspace. The response then carries it in `apiKey`, with its full value shown only once.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**permission** | [**PermissionEnum**](#PermissionEnum) |  |  [optional] |
|**expiresIn** | **Integer** | Days until expiry. |  [optional] |
|**disabledResourceGroups** | [**List&lt;DisabledResourceGroupsEnum&gt;**](#List&lt;DisabledResourceGroupsEnum&gt;) |  |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| READ_WRITE | &quot;read-write&quot; |
| READ | &quot;read&quot; |



## Enum: List&lt;DisabledResourceGroupsEnum&gt;

| Name | Value |
|---- | -----|
| PUBLISHING | &quot;publishing&quot; |
| ENGAGEMENT | &quot;engagement&quot; |
| MESSAGES | &quot;messages&quot; |
| CONTACTS | &quot;contacts&quot; |
| ANALYTICS | &quot;analytics&quot; |
| ADS | &quot;ads&quot; |
| TELEPHONY | &quot;telephony&quot; |
| ACCOUNTS | &quot;accounts&quot; |
| BILLING | &quot;billing&quot; |
| WEBHOOKS | &quot;webhooks&quot; |
| COMMERCE | &quot;commerce&quot; |
| CREATOR_CAMPAIGNS | &quot;creator_campaigns&quot; |
| MONEY | &quot;money&quot; |
| CALENDAR | &quot;calendar&quot; |
| FILES | &quot;files&quot; |



