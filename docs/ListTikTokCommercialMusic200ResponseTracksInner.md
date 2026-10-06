

# ListTikTokCommercialMusic200ResponseTracksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The full track&#39;s song clip id. Accepted as musicSoundId, but prefer clip.id: posts published with this id have shown viewers a sound page saying the song is not available in their country (observed from Germany). TikTok rejects the commercial music id itself at publish time. |  [optional] |
|**commercialMusicId** | **String** | TikTok&#39;s commercial_music_id, for reference only |  [optional] |
|**name** | **String** |  |  [optional] |
|**artist** | **String** |  |  [optional] |
|**durationSec** | **Integer** |  |  [optional] |
|**genres** | **List&lt;String&gt;** |  |  [optional] |
|**previewUrl** | **String** | Preview audio of the full track |  [optional] |
|**thumbnailUrl** | **String** |  |  [optional] |
|**rank** | **Integer** | Position in the trending chart, 1 first |  [optional] |
|**clip** | [**ListTikTokCommercialMusic200ResponseTracksInnerClip**](ListTikTokCommercialMusic200ResponseTracksInnerClip.md) |  |  [optional] |



