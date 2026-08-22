

# AnalyticsListResponsePostsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**latePostId** | **String** | Original Zernio post ID if scheduled via Zernio |  [optional] |
|**content** | **String** |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** |  |  [optional] |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**analytics** | [**PostAnalytics**](PostAnalytics.md) |  |  [optional] |
|**platforms** | [**List&lt;PlatformAnalytics&gt;**](PlatformAnalytics.md) |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**platformPostUrl** | **URI** |  |  [optional] |
|**isExternal** | **Boolean** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**thumbnailUrl** | **URI** |  |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  [optional] |
|**mediaItems** | [**List&lt;AnalyticsListResponsePostsInnerMediaItemsInner&gt;**](AnalyticsListResponsePostsInnerMediaItemsInner.md) | All media items for this post. Carousel posts contain one entry per slide. |  [optional] |
|**mediaProductType** | **String** | Instagram only: the platform media product type (e.g. FEED, REELS, STORY, AD). Absent when the platform did not report it. |  [optional] |
|**isAiGenerated** | **Boolean** | Instagram only: whether Instagram labeled the media as AI-generated. Absent when the platform did not report it. |  [optional] |
|**isSharedToFeed** | **Boolean** | Instagram reels only: whether the reel is also shared to the main feed. Absent when the platform did not report it. |  [optional] |
|**mediaAudioType** | **String** | Instagram only: audio type of the media (MUSIC or ORIGINAL_SOUND). Absent when the platform did not report it. |  [optional] |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| GIF | &quot;gif&quot; |
| DOCUMENT | &quot;document&quot; |
| CAROUSEL | &quot;carousel&quot; |
| TEXT | &quot;text&quot; |



