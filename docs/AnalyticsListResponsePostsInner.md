

# AnalyticsListResponsePostsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**latePostId** | **String** | Original Zernio post ID if scheduled via Zernio |  [optional] |
|**content** | **String** |  |  [optional] |
|**contentNotRetained** | **Boolean** | True when this team does not retain content, so the content fields of this row are null. Identifiers and metadata stay. |  [optional] |
|**scheduledFor** | **OffsetDateTime** |  |  [optional] |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**analytics** | [**PostAnalytics**](PostAnalytics.md) |  |  [optional] |
|**platforms** | [**List&lt;PlatformAnalytics&gt;**](PlatformAnalytics.md) |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**platformPostUrl** | **URI** |  |  [optional] |
|**isExternal** | **Boolean** |  |  [optional] |
|**isAd** | **Boolean** | True when this post&#39;s metrics include paid delivery, so organic reporting should exclude it.  Set for LinkedIn dark posts and for TikTok posts one of your TikTok ads promotes (Spark / boosted).  TikTok exposes no ad flag of its own. A video created by an uploaded-asset (non-Spark) TikTok ad is posted to the profile with a fresh organic id and cannot be detected, so those still report false.  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**thumbnailUrl** | **URI** | Cover image URL. A Facebook, Instagram or TikTok cover whose signed CDN link is still valid is served as that link, which expires (Meta &#x60;oe&#x3D;&#x60;, TikTok &#x60;x-expires&#x3D;&#x60;): download the image rather than storing the link.  Once the link expires, Zernio re-reads the cover from the platform and serves it from Zernio storage, a URL that does not expire.  Null while that re-read is pending (read again shortly) or when the platform no longer returns the post, never an expired link. |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  [optional] |
|**mediaItems** | [**List&lt;AnalyticsListResponsePostsInnerMediaItemsInner&gt;**](AnalyticsListResponsePostsInnerMediaItemsInner.md) | All media items for this post. Carousel posts contain one entry per slide.  - Facebook and Instagram images and video covers whose Meta CDN links expired are re-read and served from Zernio storage (non-expiring). - Facebook and Instagram video file URLs, and LinkedIn media URLs, stay the platform&#39;s signed links and are refreshed on read once they lapse. - A &#x60;url&#x60; or &#x60;thumbnail&#x60; whose platform link expired and could not be re-read yet is null, never the expired link.  |  [optional] |
|**mediaProductType** | **String** | Instagram only: the platform media product type (e.g. FEED, REELS, STORY, AD). Absent when the platform did not report it. |  [optional] |
|**isAiGenerated** | **Boolean** | Instagram only: whether Instagram labeled the media as AI-generated. Absent when the platform did not report it. |  [optional] |
|**isSharedToFeed** | **Boolean** | Instagram reels only: whether the reel is also shared to the main feed. Absent when the platform did not report it. |  [optional] |
|**mediaAudioType** | **String** | Instagram only: audio type of the media (MUSIC or ORIGINAL_SOUND). Absent when the platform did not report it. |  [optional] |
|**upcomingStartAt** | **OffsetDateTime** | YouTube only. Start time of an upcoming Premiere or scheduled live stream. Absent once it airs. While it is present, publishedAt is the upload time; after it airs, publishedAt is the time it actually started. |  [optional] |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| GIF | &quot;gif&quot; |
| DOCUMENT | &quot;document&quot; |
| CAROUSEL | &quot;carousel&quot; |
| TEXT | &quot;text&quot; |



