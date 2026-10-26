

# InstagramVideoFallback

Meta only. Present when Meta refused an existing Instagram video as the boosted ad (code 100, subcode 1815279: upload it to Facebook first) and Zernio created the ad another way. `instagram_video_reuploaded`: the video was copied into the ad account and the ad still references the original post. `instagram_video_rehosted_copy`: the video was uploaded as a new Facebook video in a new Page post, so the ad does not show the original post's likes and comments. Send `rehostOnInstagramVideoRejection: false` on the boost to get Meta's error instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**linkedToOriginalPost** | **Boolean** | True when the ad still references the original Instagram post and keeps its engagement. |  |
|**videoId** | **String** | The Facebook-side ad video Zernio made. With instagram_video_reuploaded it is the copy in the ad account video library (possibly one made by an earlier boost of the same media, reused); the creative carries it as video_id unless Meta accepted the plain post reference once the copy existed, in which case the copy is kept for that reference. With instagram_video_rehosted_copy it is the new upload the creative uses (an unused copy made by this request is deleted). |  |
|**platformError** | [**InstagramVideoFallbackPlatformError**](InstagramVideoFallbackPlatformError.md) |  |  |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| INSTAGRAM_VIDEO_REUPLOADED | &quot;instagram_video_reuploaded&quot; |
| INSTAGRAM_VIDEO_REHOSTED_COPY | &quot;instagram_video_rehosted_copy&quot; |



