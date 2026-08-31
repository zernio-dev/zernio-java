

# Post


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**userId** | [**PostUserId**](PostUserId.md) |  |  [optional] |
|**title** | **String** | Stored on the post for reference/display only. This field is NOT used as the video title when publishing. To set a YouTube video title, use platformSpecificData.title on the youtube platform target (falls back to the first line of content when omitted). |  [optional] |
|**content** | **String** |  |  [optional] |
|**mediaItems** | [**List&lt;MediaItem&gt;**](MediaItem.md) |  |  [optional] |
|**platforms** | [**List&lt;PlatformTarget&gt;**](PlatformTarget.md) |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** |  |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | **List&lt;String&gt;** | YouTube constraints: each tag max 100 chars, combined max 500 chars, duplicates removed. |  [optional] |
|**hashtags** | **List&lt;String&gt;** | Stored for reference only. Hashtags are NOT automatically appended to the caption when publishing. Include hashtags directly in the content field (platforms like Instagram only support hashtags as caption text). For YouTube keywords, use the tags field instead. |  [optional] |
|**mentions** | **List&lt;String&gt;** | Stored for reference only. This field does NOT automatically create @mentions when publishing. For LinkedIn @mentions, use the /v1/accounts/{accountId}/linkedin-mentions endpoint to resolve profile URLs to URNs, then embed the returned mentionFormat directly in the post content field. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**recycling** | [**RecyclingState**](RecyclingState.md) |  |  [optional] |
|**recycledFromPostId** | **String** | ID of the original post if this post was created via recycling |  [optional] |
|**queuedFromProfile** | **String** | Profile ID if the post was scheduled via the queue |  [optional] |
|**queueId** | **String** | Queue ID if the post was scheduled via a specific queue |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| PUBLISHING | &quot;publishing&quot; |
| PUBLISHED | &quot;published&quot; |
| FAILED | &quot;failed&quot; |
| PARTIAL | &quot;partial&quot; |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| PRIVATE | &quot;private&quot; |
| UNLISTED | &quot;unlisted&quot; |



