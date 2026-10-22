

# ListInboxMentions200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Mention document ID |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Instagram only: &#x60;caption&#x60; when the account was tagged in a media caption, &#x60;comment&#x60; when it was tagged in a comment. Null for LinkedIn. |  [optional] |
|**mediaId** | **String** | Instagram only: ID of the media the account was mentioned in (or under). Null for LinkedIn. |  [optional] |
|**commentId** | **String** | Instagram only: ID of the comment that mentioned the account. Null for caption mentions and LinkedIn. |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**content** | **String** | Text that mentioned you: the post text on LinkedIn, the caption or comment text on Instagram. Empty until it has been read. |  [optional] |
|**permalink** | **String** | URL to the source post on LinkedIn. Null on Instagram. |  [optional] |
|**authorUrn** | **String** | LinkedIn URN of the person who mentioned you, or the Instagram-scoped ID of the commenter on an Instagram comment mention. |  [optional] |
|**authorName** | **String** | Display name of the author, resolved from authorUrn. Null when LinkedIn does not allow resolving the profile. |  [optional] |
|**authorUsername** | **String** | LinkedIn vanity name of the author (the slug in their profile URL), or the Instagram username of the commenter or media owner. |  [optional] |
|**authorPicture** | **String** | Profile picture URL of the author. LinkedIn CDN URLs expire after some time, so fetch promptly rather than storing long-term. |  [optional] |
|**organizationalEntity** | **String** | URN of the LinkedIn organization that was mentioned, or the Instagram user ID of the mentioned account. |  [optional] |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| LINKEDIN | &quot;linkedin&quot; |
| INSTAGRAM | &quot;instagram&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAPTION | &quot;caption&quot; |
| COMMENT | &quot;comment&quot; |



