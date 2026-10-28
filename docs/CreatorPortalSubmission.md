

# CreatorPortalSubmission


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**platform** | **String** |  |  |
|**postId** | **String** |  |  |
|**url** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**submittedAt** | **OffsetDateTime** |  |  |
|**publishedAt** | **OffsetDateTime** |  |  |
|**views** | **Integer** | Latest view count read for the post. |  |
|**earnedCents** | **Integer** |  |  |
|**rejectReason** | **String** |  |  |
|**flags** | [**List&lt;FlagsEnum&gt;**](#List&lt;FlagsEnum&gt;) | Creator-safe flags only. Every other review flag shows as &#x60;under_review&#x60;. |  |
|**trackingEndsAt** | **OffsetDateTime** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RECEIVED | &quot;received&quot; |
| TRACKING | &quot;tracking&quot; |
| PENDING_REVIEW | &quot;pending_review&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |
| EXPIRED | &quot;expired&quot; |
| WITHDRAWN | &quot;withdrawn&quot; |



## Enum: List&lt;FlagsEnum&gt;

| Name | Value |
|---- | -----|
| UNREACHABLE | &quot;unreachable&quot; |
| POST_DELETED | &quot;post_deleted&quot; |
| DUPLICATE_POST | &quot;duplicate_post&quot; |
| UNDER_REVIEW | &quot;under_review&quot; |



