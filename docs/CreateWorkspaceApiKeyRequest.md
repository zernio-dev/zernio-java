

# CreateWorkspaceApiKeyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**permission** | [**PermissionEnum**](#PermissionEnum) | &#39;read&#39; restricts the key to GET requests. |  [optional] |
|**expiresIn** | **Integer** | Days until expiry. Omit for a key that never expires. |  [optional] |
|**disabledResourceGroups** | [**List&lt;DisabledResourceGroupsEnum&gt;**](#List&lt;DisabledResourceGroupsEnum&gt;) | Resource groups the key cannot use, as on &#x60;POST /v1/api-keys&#x60;. |  [optional] |



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



