

# InstagramBusinessDiscoveryMediaInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**caption** | **String** |  |  |
|**mediaType** | **String** | IMAGE, VIDEO or CAROUSEL_ALBUM |  |
|**mediaProductType** | **String** | FEED or REELS |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**permalink** | **String** |  |  |
|**likeCount** | **Integer** | Null when the owner hides like counts |  |
|**commentsCount** | **Integer** |  |  |
|**mediaUrl** | **String** | Temporary CDN URL that expires; download the file rather than storing the link. Null on videos whose audio is licensed music, use thumbnailUrl for the cover. |  |
|**thumbnailUrl** | **String** | Video cover frame, VIDEO only. Temporary CDN URL. |  |
|**viewCount** | **Integer** | Reels only. Null on images and carousels. |  |
|**children** | [**List&lt;InstagramBusinessDiscoveryMediaInnerChildrenInner&gt;**](InstagramBusinessDiscoveryMediaInnerChildrenInner.md) | Carousel slides in order. Null unless mediaType is CAROUSEL_ALBUM. |  |



