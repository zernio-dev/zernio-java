

# WebhookPayloadPostPostPlatformsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** |  |  |
|**status** | **String** |  |  |
|**accountId** | **String** | SocialAccount id this platform target published through. Use it to route events by connected account (e.g. separate staging vs production endpoints). A post can span multiple accounts. |  [optional] |
|**platformPostId** | **String** |  |  [optional] |
|**publishedUrl** | **String** |  |  [optional] |
|**error** | **String** |  |  [optional] |
|**errorCategory** | [**ErrorCategoryEnum**](#ErrorCategoryEnum) | Present when this target failed. Same taxonomy as &#x60;platforms[].errorCategory&#x60; on GET /v1/posts. |  [optional] |
|**errorSource** | [**ErrorSourceEnum**](#ErrorSourceEnum) | Present when this target failed. Who must act: user, platform or system (Zernio). |  [optional] |
|**platformError** | [**PostPlatformError**](PostPlatformError.md) |  |  [optional] |



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



