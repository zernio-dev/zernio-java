

# CreateWorkspace201ResponseApiKeyError

Present only when `apiKey` is null. The workspace exists; create its key from the dashboard instead of retrying the call, which would create a second workspace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) |  |  [optional] |
|**message** | **String** |  |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| API_KEY_NOT_CREATED | &quot;api_key_not_created&quot; |



