

# ErrorResponse

Canonical error envelope. `error` is the human-readable message; `type`, `code`, `param`, `platform`, and `platformError` are top-level siblings for programmatic handling. For upstream platform failures (`type: platform_error`), `platformError` carries the provider's raw payload verbatim (for Meta: `error_subcode`, `error_user_title`, `error_user_msg`). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | **String** | Human-readable error message. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Error class for programmatic handling. |  [optional] |
|**code** | **String** | Stable machine-readable error code. |  [optional] |
|**param** | **String** | The request field that caused the error, when applicable. |  [optional] |
|**docUrl** | **String** | Documentation page for resolving the error, when one applies. |  [optional] |
|**platform** | **String** | Upstream platform (e.g. meta, google, tiktok), present when type is platform_error. |  [optional] |
|**platformError** | **Map&lt;String, Object&gt;** | Raw error payload from the upstream platform, passed through verbatim so integrators can read provider-specific codes. For Meta this includes error_subcode, error_user_title, and error_user_msg.  |  [optional] |
|**provider** | **String** | Email API: the mailbox provider the error came from (&#x60;google&#x60;, &#x60;microsoft&#x60;). |  [optional] |
|**providerError** | [**ErrorResponseProviderError**](ErrorResponseProviderError.md) |  |  [optional] |
|**retryable** | **Boolean** | Email API: whether the same request can succeed if retried (with the same &#x60;Idempotency-Key&#x60; for sends). |  [optional] |
|**requestId** | **String** | Email API: the request id, also in the &#x60;X-Request-Id&#x60; header. Quote it when you contact support. |  [optional] |
|**docsUrl** | **String** | Email API: where this &#x60;code&#x60; is documented. |  [optional] |
|**details** | **ErrorResponseDetails** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INVALID_REQUEST_ERROR | &quot;invalid_request_error&quot; |
| AUTHENTICATION_ERROR | &quot;authentication_error&quot; |
| PERMISSION_ERROR | &quot;permission_error&quot; |
| NOT_FOUND | &quot;not_found&quot; |
| RATE_LIMIT_ERROR | &quot;rate_limit_error&quot; |
| PLATFORM_ERROR | &quot;platform_error&quot; |
| API_ERROR | &quot;api_error&quot; |



