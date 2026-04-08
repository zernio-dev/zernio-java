

# ListLogs200ResponseLogsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | Log category (publishing, connections, webhooks, messaging) |  [optional] |
|**action** | **String** | Specific action (post.published, message.sent, account.connected, etc.) |  [optional] |
|**userId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**statusCode** | **Integer** |  |  [optional] |
|**errorMessage** | **String** |  |  [optional] |
|**errorCode** | **String** |  |  [optional] |
|**durationMs** | **Integer** |  |  [optional] |
|**endpoint** | **String** | The API endpoint that triggered this log |  [optional] |
|**requestBody** | **String** | Request JSON (truncated to 5KB) |  [optional] |
|**responseBody** | **String** | Response JSON (truncated to 10KB) |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**metadata** | **String** | Additional context as JSON string |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILED | &quot;failed&quot; |
| PENDING | &quot;pending&quot; |
| SKIPPED | &quot;skipped&quot; |



