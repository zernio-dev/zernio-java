

# WebhookPayloadPostPlatformPlatform

The specific platform that transitioned to a terminal state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Platform name (e.g. &#x60;twitter&#x60;, &#x60;tiktok&#x60;, &#x60;instagram&#x60;). |  |
|**status** | [**StatusEnum**](#StatusEnum) | Terminal status this event fires on. Matches the event suffix. |  |
|**platformPostId** | **String** | Platform-native post id. Present on &#x60;published&#x60; and &#x60;deleted&#x60;, absent on &#x60;failed&#x60;. |  [optional] |
|**publishedUrl** | **String** | Public URL to the platform-side post. Present on &#x60;published&#x60; (when the platform exposes one and it is not a draft) and on &#x60;deleted&#x60; (when one was recorded at publish time). |  [optional] |
|**error** | **String** | Error message from the platform. Present on &#x60;failed&#x60; only. |  [optional] |
|**errorCategory** | [**ErrorCategoryEnum**](#ErrorCategoryEnum) | Error category for programmatic handling. Present on &#x60;failed&#x60; only. Same taxonomy as &#x60;platforms[].errorCategory&#x60; on GET /v1/posts. |  [optional] |
|**errorSource** | [**ErrorSourceEnum**](#ErrorSourceEnum) | Who must act on the failure: user (fix content or reconnect), platform (outage or policy), system (Zernio). Present on &#x60;failed&#x60; only. |  [optional] |
|**deletedAt** | **OffsetDateTime** | When the platform-side deletion was detected by Zernio sync (ISO 8601). Present only on &#x60;post.platform.deleted&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;published&quot; |
| FAILED | &quot;failed&quot; |
| DELETED | &quot;deleted&quot; |



## Enum: ErrorCategoryEnum

| Name | Value |
|---- | -----|
| AUTH_EXPIRED | &quot;auth_expired&quot; |
| USER_CONTENT | &quot;user_content&quot; |
| USER_ABUSE | &quot;user_abuse&quot; |
| ACCOUNT_ISSUE | &quot;account_issue&quot; |
| PLATFORM_REJECTED | &quot;platform_rejected&quot; |
| PLATFORM_ERROR | &quot;platform_error&quot; |
| PLATFORM_RATE_LIMIT | &quot;platform_rate_limit&quot; |
| QUOTA_EXHAUSTED | &quot;quota_exhausted&quot; |
| SYSTEM_ERROR | &quot;system_error&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: ErrorSourceEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| PLATFORM | &quot;platform&quot; |
| SYSTEM | &quot;system&quot; |



