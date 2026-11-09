

# BalanceRequiredError

The error envelope of a $0 balance refusal (402 `insufficient_balance` or `usage_limit_reached`), plus where to fund the balance.

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
|**details** | **ErrorResponseDetails** |  |  [optional] |
|**fundingUrl** | **URI** | Dashboard link to Billing that opens the Add funds drawer (the add-card drawer first when there is no card). Send the user there, then retry. |  |



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



