

# UpdatePostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  [optional] |
|**content** | **String** |  |  [optional] |
|**mediaItems** | [**List&lt;MediaItem&gt;**](MediaItem.md) |  |  [optional] |
|**platforms** | [**List&lt;UpdatePostRequestPlatformsInner&gt;**](UpdatePostRequestPlatformsInner.md) | Target platforms and accounts for this post. Each item must include platform and accountId. |  [optional] |
|**scheduledFor** | **OffsetDateTime** |  |  [optional] |
|**publishNow** | **Boolean** |  |  [optional] |
|**isDraft** | **Boolean** |  |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**hashtags** | **List&lt;String&gt;** |  |  [optional] |
|**mentions** | **List&lt;String&gt;** |  |  [optional] |
|**crosspostingEnabled** | **Boolean** |  |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**queuedFromProfile** | **String** | Profile ID to schedule via queue. |  [optional] |
|**queueId** | **String** | Specific queue ID to use when scheduling via queue. |  [optional] |
|**tiktokSettings** | [**TikTokPlatformData**](TikTokPlatformData.md) | Root-level TikTok settings applied to all TikTok platforms. Merged into each platform&#39;s platformSpecificData, with platform-specific settings taking precedence. |  [optional] |
|**facebookSettings** | [**FacebookPlatformData**](FacebookPlatformData.md) | Root-level Facebook settings applied to all Facebook platforms. Merged into each platform&#39;s platformSpecificData, with platform-specific settings taking precedence. |  [optional] |
|**recycling** | [**RecyclingConfig**](RecyclingConfig.md) |  |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| PRIVATE | &quot;private&quot; |
| UNLISTED | &quot;unlisted&quot; |



