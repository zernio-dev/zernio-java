

# PreflightBrandedCallingIdentity200ResponseFindingsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  [optional] |
|**field** | **String** | The body field the finding is about, e.g. references.financial.email. |  [optional] |
|**message** | **String** |  |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| DISPLAY_NAME_MISMATCH | &quot;display-name-mismatch&quot; |
| CALL_REASONS_MANUAL | &quot;call-reasons-manual&quot; |
| AUTHORIZER_FREE_MAIL | &quot;authorizer-free-mail&quot; |
| AUTHORIZER_DOMAIN_MISMATCH | &quot;authorizer-domain-mismatch&quot; |
| REFERENCE_PHONE_DUPLICATE | &quot;reference-phone-duplicate&quot; |
| REFERENCE_INTERNAL | &quot;reference-internal&quot; |
| REFERENCE_FINANCIAL_FREE_MAIL | &quot;reference-financial-free-mail&quot; |
| REFERENCE_TIMEZONE_INVALID | &quot;reference-timezone-invalid&quot; |
| LOGO_UNREACHABLE | &quot;logo-unreachable&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| BLOCK | &quot;block&quot; |
| WARN | &quot;warn&quot; |



