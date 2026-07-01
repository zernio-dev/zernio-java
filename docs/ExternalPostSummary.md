

# ExternalPostSummary

A post synced from a platform (published directly on the platform, not through Zernio). Returned by GET /v1/posts?source=external and POST /v1/posts/sync-external. Analytics are exposed separately via GET /v1/analytics?source=external. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** | Platform the post belongs to (e.g. instagram, youtube, tiktok) |  [optional] |
|**platformPostId** | **String** | The platform&#39;s own post/media/video id |  [optional] |
|**platformPostUrl** | **String** | Canonical URL (permalink) of the post on the platform |  [optional] |
|**content** | **String** | Post caption / text |  [optional] |
|**publishedAt** | **OffsetDateTime** | When the post was published on the platform |  [optional] |
|**mediaType** | **String** | Media type (e.g. image, video, carousel) |  [optional] |
|**mediaUrl** | **String** | Primary media URL |  [optional] |
|**thumbnailUrl** | **String** | Thumbnail URL |  [optional] |
|**mediaItems** | **List&lt;Object&gt;** | Per-item media (for carousels / multi-media posts) |  [optional] |
|**analytics** | [**ExternalPostSummaryAnalytics**](ExternalPostSummaryAnalytics.md) |  |  [optional] |



