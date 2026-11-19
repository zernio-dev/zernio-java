

# WebhookPayloadAccountRestrictedRestriction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | [**ReasonEnum**](#ReasonEnum) | &#x60;suspended&#x60;: banned or suspended by the platform. &#x60;restricted&#x60;: locked, restricted or blocked from posting. &#x60;verification_required&#x60;: the platform asks for an identity or security check. &#x60;auth_expired&#x60;: the login stopped working; reconnect. |  |
|**message** | **String** | The error the last failed post carries. |  |
|**platformError** | [**WebhookPayloadAccountRestrictedRestrictionPlatformError**](WebhookPayloadAccountRestrictedRestrictionPlatformError.md) |  |  |
|**consecutiveFailures** | **Integer** | Identical failures in a row that restricted the account. |  |
|**since** | **OffsetDateTime** |  |  |
|**postId** | **String** | The post whose failure restricted the account. |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| RESTRICTED | &quot;restricted&quot; |
| SUSPENDED | &quot;suspended&quot; |
| VERIFICATION_REQUIRED | &quot;verification_required&quot; |
| AUTH_EXPIRED | &quot;auth_expired&quot; |



