

# GetYoutubeCaptions200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**videoId** | **String** |  |  [optional] |
|**language** | **String** | The language of the returned track. |  [optional] |
|**trackId** | **String** | YouTube&#39;s own caption track id. |  [optional] |
|**trackKind** | [**TrackKindEnum**](#TrackKindEnum) | &#x60;asr&#x60; is YouTube&#39;s auto-generated track; &#x60;standard&#x60; was uploaded by the channel. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | &#x60;cache&#x60; when served from our stored copy, &#x60;youtube&#x60; when this call spent the quota units. |  [optional] |
|**fetchedAt** | **OffsetDateTime** | When the stored copy was downloaded from YouTube. |  [optional] |
|**text** | **String** | The whole transcript as one paragraph, no timings. |  [optional] |
|**cues** | [**List&lt;GetYoutubeCaptions200ResponseCuesInner&gt;**](GetYoutubeCaptions200ResponseCuesInner.md) | Timed cues. Present when format is json. Auto-generated cues overlap in time by design (captions roll), so &#x60;start&#x60; can precede the previous cue&#39;s &#x60;end&#x60;. |  [optional] |
|**srt** | **String** | Raw SubRip body. Present when format is srt. |  [optional] |
|**availableTracks** | [**List&lt;GetYoutubeCaptions200ResponseAvailableTracksInner&gt;**](GetYoutubeCaptions200ResponseAvailableTracksInner.md) | Every track on the video, so you can re-request another language. On a cached read this is the listing as it stood when we downloaded, so a language added to the video since then appears only after a &#x60;refresh&#x3D;true&#x60; or when you request that language directly. |  [optional] |



## Enum: TrackKindEnum

| Name | Value |
|---- | -----|
| ASR | &quot;asr&quot; |
| STANDARD | &quot;standard&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| CACHE | &quot;cache&quot; |
| YOUTUBE | &quot;youtube&quot; |



