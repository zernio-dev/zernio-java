

# CommentAttachment

Facebook only. The media on a comment (sticker, GIF, photo, shared link or video). One attachment per comment, a single object. URLs are expiring Meta CDN links (oe= expiry), so fetch promptly. Instagram comments carry no media. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | Attachment type as Facebook reports it, for example sticker, animated_image_share, photo, image_share, share or video_inline. |  |
|**imageUrl** | **String** | Rendered image/preview URL (from attachment.media.image.src). |  [optional] |
|**url** | **String** | Source URL (from attachment.url). For GIFs this is an l.facebook.com redirect. |  [optional] |



