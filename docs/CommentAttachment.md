

# CommentAttachment

The media on a comment or reply, one per comment (the first item when the platform returns several). `type` is the platform's own media kind:  - Facebook: sticker, animated_image_share, photo, image_share, share or video_inline. - TikTok: image. - X: photo, video or animated_gif. A video `url` is an mp4 and `imageUrl` its preview. - Threads: IMAGE, VIDEO or GIF. Album replies carry no attachment. - Bluesky: image, video or external (link cards, GIFs arrive this way). A video `url` is an HLS playlist (.m3u8).  Facebook and Threads URLs are expiring Meta CDN links, so fetch promptly. Instagram, YouTube, LinkedIn and Reddit comments carry no media. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | The platform&#39;s own media kind, see the schema description for each platform&#39;s values. |  |
|**imageUrl** | **String** | Rendered image or preview URL. |  [optional] |
|**url** | **String** | Source or playable URL. Facebook GIFs carry an l.facebook.com redirect, X videos an mp4, Bluesky videos an HLS playlist. |  [optional] |



