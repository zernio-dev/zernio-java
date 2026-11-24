

# VerifyCredential200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**valid** | **Boolean** |  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**name** | **String** | Display name of the credential&#39;s owner. |  [optional] |
|**email** | **String** | Email of the credential&#39;s owner. |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) |  |  [optional] |
|**scope** | **String** | Granted OAuth scopes, space-separated. Null for API keys. |  [optional] |
|**audience** | **String** | Resource the OAuth token was issued for (RFC 8707), for example https://mcp.zernio.com/mcp. Null for API keys and for tokens issued without one. |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| API_KEY | &quot;api_key&quot; |
| OAUTH | &quot;oauth&quot; |
| SESSION | &quot;session&quot; |



