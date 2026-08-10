

# InstagramPlatformDataAudioConfiguration

Attach a licensed music track or original sound from the Instagram audio catalog to a Reel. Reels only (single video post, not a story or image). Requires an Instagram account connected via Facebook Login; classic Instagram Login accounts get a 400 (instagram_audio_requires_facebook_login). Get audio IDs from GET /v1/accounts/{accountId}/instagram/audio. If the track becomes unavailable by publish time (removed, region-blocked, licensing change), the post fails with a user-error; it is not published without the audio.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioId** | **String** | Audio asset ID from the audio search endpoint. |  |
|**audioVolume** | **Integer** | Volume of the attached audio track, 0-100. Defaults to 100. |  [optional] |
|**videoVolume** | **Integer** | Volume of the video&#39;s own sound, 0-100. Defaults to 100. Set 0 to mute the original video audio. |  [optional] |



