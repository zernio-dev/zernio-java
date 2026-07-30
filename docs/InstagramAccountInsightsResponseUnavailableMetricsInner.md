

# InstagramAccountInsightsResponseUnavailableMetricsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | **String** | The requested metric name. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | \&quot;not_enrolled\&quot;: the account is not enrolled in the program behind this metric. \&quot;permission_missing\&quot;: the connected user lacks access to this metric. \&quot;unsupported_metric\&quot;: the platform does not accept this metric name on the API version Zernio uses. \&quot;no_data\&quot;: the platform returned no bucket for this metric over the requested range. \&quot;unreadable_value\&quot;: the platform returned a value shape Zernio cannot read, so no total is reported. \&quot;mixed_currency\&quot;: readable values disagree on currency or unit within the range. \&quot;upstream_error\&quot;: any other platform failure.  \&quot;no_data\&quot; is the common case in practice. The others are defensive: \&quot;not_enrolled\&quot; and \&quot;unsupported_metric\&quot; in particular have not been observed on live Facebook traffic, since a non-enrolled Page returns zeros rather than an error and metric names are validated before any platform call.  |  [optional] |
|**message** | **String** | Platform-provided explanation when available (access tokens redacted), otherwise Zernio copy. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| NOT_ENROLLED | &quot;not_enrolled&quot; |
| PERMISSION_MISSING | &quot;permission_missing&quot; |
| UNSUPPORTED_METRIC | &quot;unsupported_metric&quot; |
| NO_DATA | &quot;no_data&quot; |
| UNREADABLE_VALUE | &quot;unreadable_value&quot; |
| MIXED_CURRENCY | &quot;mixed_currency&quot; |
| UPSTREAM_ERROR | &quot;upstream_error&quot; |



