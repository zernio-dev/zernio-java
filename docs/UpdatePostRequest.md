

# UpdatePostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | Stored on the post for reference/display only. This field is NOT used as the video title when publishing. To set a YouTube video title, use platformSpecificData.title on the youtube platform target (falls back to the first line of content when omitted). |  [optional] |
|**content** | **String** |  |  [optional] |
|**mediaItems** | [**List&lt;MediaItem&gt;**](MediaItem.md) |  |  [optional] |
|**platforms** | [**List&lt;UpdatePostRequestPlatformsInner&gt;**](UpdatePostRequestPlatformsInner.md) | Target platforms and accounts for this post. Each item must include platform and accountId. |  [optional] |
|**scheduledFor** | **OffsetDateTime** |  |  [optional] |
|**publishNow** | **Boolean** |  |  [optional] |
|**isDraft** | **Boolean** | When omitted, the post keeps its current draft status. Send &#x60;false&#x60; to promote a draft to scheduled (combined with &#x60;scheduledFor&#x60;, &#x60;publishNow&#x60;, or a queue). |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**hashtags** | **List&lt;String&gt;** | Stored for reference only. Hashtags are NOT automatically appended to the caption when publishing. Include hashtags directly in the content field (platforms like Instagram only support hashtags as caption text). For YouTube keywords, use the tags field instead. |  [optional] |
|**mentions** | **List&lt;String&gt;** |  |  [optional] |
|**crosspostingEnabled** | **Boolean** |  |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**queuedFromProfile** | **String** | Profile ID to schedule via queue. |  [optional] |
|**queueId** | **String** | Specific queue ID to use when scheduling via queue. |  [optional] |
|**tiktokSettings** | [**TikTokPlatformData**](TikTokPlatformData.md) | Root-level TikTok settings applied to the TikTok platforms sent in the same request. Merged into each platform&#39;s platformSpecificData, with platform-specific settings taking precedence. Returns 400 if sent without a platforms array. |  [optional] |
|**facebookSettings** | [**FacebookSettings**](FacebookSettings.md) | Root-level Facebook settings applied to the Facebook platforms sent in the same request. Merged into each platform&#39;s platformSpecificData.facebookSettings, with platform-specific settings taking precedence. Returns 400 if sent without a platforms array. |  [optional] |
|**recycling** | [**RecyclingConfig**](RecyclingConfig.md) |  |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| PRIVATE | &quot;private&quot; |
| UNLISTED | &quot;unlisted&quot; |



