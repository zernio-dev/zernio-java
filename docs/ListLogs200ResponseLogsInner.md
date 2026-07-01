

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
|**requestId** | **String** | Correlation ID linking every log from one API request (api_request logs) |  [optional] |
|**apiKeyId** | **String** | The API key that made the request (api_request logs) |  [optional] |
|**method** | **String** | HTTP method (api_request logs) |  [optional] |
|**path** | **String** | Request path (api_request logs) |  [optional] |
|**ipAddress** | **String** | Client IP address (api_request logs) |  [optional] |
|**userAgent** | **String** | Client user-agent (api_request logs) |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILED | &quot;failed&quot; |
| PENDING | &quot;pending&quot; |
| SKIPPED | &quot;skipped&quot; |



