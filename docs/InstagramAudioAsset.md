

# InstagramAudioAsset

One asset from the Instagram audio catalog. Licensed music carries artist/artwork fields; original sounds carry creator fields instead, so most fields are nullable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioId** | **String** | Audio asset ID. Pass it as platformSpecificData.audioConfiguration.audioId when creating a Reel. |  [optional] |
|**title** | **String** | Track or sound title. |  [optional] |
|**audioType** | [**AudioTypeEnum**](#AudioTypeEnum) | Catalog type of the asset. |  [optional] |
|**durationInMs** | **Integer** | Asset duration in milliseconds. |  [optional] |
|**displayArtist** | **String** | Artist name (licensed music only). |  [optional] |
|**coverArtworkThumbnailUrl** | **String** | Cover artwork thumbnail (licensed music only). |  [optional] |
|**downloadUrl** | **String** | Temporary preview URL. Meta expires it after roughly 1.5 days; re-fetch the asset to refresh it. |  [optional] |
|**igUsername** | **String** | Creator username (original sounds only). |  [optional] |
|**profilePictureUrl** | **String** | Creator profile picture (original sounds only). |  [optional] |
|**isAdsEligible** | **Boolean** | Whether the asset is eligible for ads use. |  [optional] |
|**onPlatformAudioPreviewLink** | **String** | Instagram web link to preview the audio. |  [optional] |



## Enum: AudioTypeEnum

| Name | Value |
|---- | -----|
| MUSIC | &quot;music&quot; |
| ORIGINAL_SOUND | &quot;original_sound&quot; |



