

# ExternalPostMediaItem

A media item on a native (external/synced) post, as carried by post.external.* webhook payloads. Distinct from the richer MediaItem used for Zernio-authored posts: external items are always already-published and limited to image or video. Kept as a separate schema so the generated SDK model does not collide with MediaItem. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**url** | **String** | &#39;Direct URL to the media file. Null when the platform withholds it: check mediaStatus before downloading. Instagram omits the video file for Reels it flags as containing copyrighted material (its docs name audio as the usual cause), so type stays \&quot;video\&quot; while the file is permanently unreachable. For LinkedIn videos where the platform returns no file, url falls back to the cover image and the item carries mediaStatus: unavailable.&#39; |  |
|**thumbnail** | **String** | Cover image. Still present when url is null. |  [optional] |
|**mediaStatus** | [**MediaStatusEnum**](#MediaStatusEnum) | &#39;Present only when the media file could not be retrieved (url is null or, for LinkedIn videos, a cover image standing in for the file). Absent means the file is available at url.&#39; |  [optional] |
|**unavailableReason** | [**UnavailableReasonEnum**](#UnavailableReasonEnum) | Why the file is missing. platform_withheld means the platform declined to return it and retrying will not help. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |



## Enum: MediaStatusEnum

| Name | Value |
|---- | -----|
| UNAVAILABLE | &quot;unavailable&quot; |



## Enum: UnavailableReasonEnum

| Name | Value |
|---- | -----|
| PLATFORM_WITHHELD | &quot;platform_withheld&quot; |



