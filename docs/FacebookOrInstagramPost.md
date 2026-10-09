

# FacebookOrInstagramPost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Facebook post id ({pageId}_{postId}) or Instagram media id |  |
|**permalink** | **URI** |  |  |
|**text** | **String** | Facebook post message or Instagram caption |  |
|**thumbnailUrl** | **URI** | Facebook &#x60;full_picture&#x60; (or the first attachment image); Instagram &#x60;thumbnail_url&#x60; for videos, &#x60;media_url&#x60; for images. Expiring Meta CDN URL. |  |
|**mediaUrl** | **URI** | Instagram &#x60;media_url&#x60; (the video file for videos). Always null on Facebook. Expiring Meta CDN URL. |  |
|**mediaType** | **String** | Instagram &#x60;media_type&#x60; (IMAGE, VIDEO, CAROUSEL_ALBUM) or the Facebook attachment type (photo, video_inline, link, ...) |  |
|**productType** | **String** | Instagram &#x60;media_product_type&#x60;: AD, FEED, REELS or STORY. Always null on Facebook. |  |
|**createdAt** | **String** | Creation time as Meta returns it (e.g. 2026-05-27T17:15:51+0000) |  |



