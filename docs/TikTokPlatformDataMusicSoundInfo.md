

# TikTokPlatformDataMusicSoundInfo

Commercial Music Library track to attach. Accounts connected through the TikTok for Business app only: a developer-app account rejects the post at publish time with a message that says so. Pick musicSoundId from GET /v1/accounts/{accountId}/tiktok/commercial-music. Ignored on drafts, where TikTok ignores every post_info field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**musicSoundId** | **String** | The id field of a track from GET /v1/accounts/{accountId}/tiktok/commercial-music (a song clip id). TikTok fails the publish with a generic 51065 when given the commercial music id instead. |  |
|**musicSoundVolume** | **Integer** | Track volume. TikTok defaults an omitted volume to 0, which publishes the track silently, so we default to the app&#39;s 50. Video posts only. |  [optional] |
|**musicSoundStart** | **Integer** | Start point of the track in milliseconds (default 0). Video posts only. |  [optional] |
|**musicSoundEnd** | **Integer** | End point of the track in milliseconds (default: the video length). Must be greater than musicSoundStart. Video posts only. |  [optional] |



