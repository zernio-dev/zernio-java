

# AnalyticsSinglePostResponseMediaItemsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**url** | **URI** | &#39;Direct URL to the media file. Null when the platform withholds it: check mediaStatus before downloading. Instagram omits the video file for Reels it flags as containing copyrighted material (its docs name audio as the usual cause), so type stays \&quot;video\&quot; while the file is permanently unreachable.&#39; |  [optional] |
|**thumbnail** | **URI** | Thumbnail URL (same as url for images). Still present when url is null. |  [optional] |
|**altText** | **String** | Accessibility alt text set on the media, when present. |  [optional] |
|**mediaStatus** | [**MediaStatusEnum**](#MediaStatusEnum) | Present only when the media file could not be retrieved. Absent means the file is available at url. |  [optional] |
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



