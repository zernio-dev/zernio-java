

# AnalyticsSinglePostResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postId** | **String** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**content** | **String** |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** |  |  [optional] |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |
|**analytics** | [**PostAnalytics**](PostAnalytics.md) |  |  [optional] |
|**platformAnalytics** | [**List&lt;PlatformAnalytics&gt;**](PlatformAnalytics.md) |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**platformPostUrl** | **URI** |  |  [optional] |
|**isExternal** | **Boolean** |  |  [optional] |
|**thumbnailUrl** | **URI** |  |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  [optional] |
|**mediaItems** | [**List&lt;AnalyticsSinglePostResponseMediaItemsInner&gt;**](AnalyticsSinglePostResponseMediaItemsInner.md) | All media items for this post. Carousel posts contain one entry per slide. |  [optional] |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| CAROUSEL | &quot;carousel&quot; |
| TEXT | &quot;text&quot; |



