

# WebhookPayloadMentionMention


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Mention ID, the same as &#x60;id&#x60; on GET /v1/inbox/mentions. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | Null on LinkedIn. |  |
|**mediaId** | **String** | Instagram media ID. |  |
|**postId** | **String** | Facebook post ID. |  |
|**commentId** | **String** |  |  |
|**content** | **String** | Text that mentioned the account. |  |
|**permalink** | **String** | URL to the source post on LinkedIn. Null on Instagram and Facebook. |  |
|**authorUrn** | **String** |  |  |
|**authorName** | **String** |  |  |
|**authorUsername** | **String** |  |  |
|**authorPicture** | **String** |  |  |
|**organizationalEntity** | **String** | The mentioned organization, Page or Instagram account. |  |
|**publishedAt** | **OffsetDateTime** |  |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| LINKEDIN | &quot;linkedin&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAPTION | &quot;caption&quot; |
| POST | &quot;post&quot; |
| COMMENT | &quot;comment&quot; |



