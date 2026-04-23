

# GetAdComments200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**adId** | **String** | Internal Zernio ad ID. |  |
|**platformAdId** | **String** | Meta ad ID. |  |
|**effectiveStoryId** | **String** | Underlying post ID the comments belong to. effective_object_story_id for Facebook, effective_instagram_media_id for Instagram. |  |
|**accountId** | **String** | Social account ID (ads SocialAccount). |  |
|**lastUpdated** | **OffsetDateTime** |  |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



