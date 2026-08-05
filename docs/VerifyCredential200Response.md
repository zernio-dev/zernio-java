

# VerifyCredential200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**valid** | **Boolean** |  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) |  |  [optional] |
|**scope** | **String** | Granted OAuth scopes, space-separated. Null for API keys. |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| API_KEY | &quot;api_key&quot; |
| OAUTH | &quot;oauth&quot; |
| SESSION | &quot;session&quot; |



