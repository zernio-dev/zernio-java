

# WebhookPayloadAccountPermissionsChangedAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**profileId** | **String** |  |  |
|**platform** | **String** |  |  |
|**username** | **String** |  |  |
|**displayName** | **String** |  |  [optional] |
|**oauthAppId** | **String** | The OAuth app the account connected through. |  |
|**missingScopeAreas** | [**List&lt;MissingScopeAreasEnum&gt;**](#List&lt;MissingScopeAreasEnum&gt;) | Every area now missing. Enable the permission on your app (or have the user grant it), then reconnect the account. |  |
|**reason** | **String** | The platform error that revealed it. |  |



## Enum: List&lt;MissingScopeAreasEnum&gt;

| Name | Value |
|---- | -----|
| POSTING | &quot;posting&quot; |
| ANALYTICS | &quot;analytics&quot; |
| COMMENTS | &quot;comments&quot; |
| MESSAGING | &quot;messaging&quot; |



