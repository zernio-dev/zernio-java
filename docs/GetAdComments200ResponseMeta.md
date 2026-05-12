

# GetAdComments200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**adId** | **String** | Internal Zernio ad ID. |  |
|**platformAdId** | **String** | Meta ad ID. |  |
|**effectiveStoryId** | **String** | Underlying post ID the comments belong to. effective_object_story_id for Facebook, effective_instagram_media_id for Instagram. |  |
|**instagramUserId** | **String** | Instagram-only. The Instagram-scoped business ID that owns the boosted media (creative.instagram_user_id). |  [optional] |
|**instagramPermalink** | **String** | Instagram-only. Public permalink of the boosted IG post (creative.instagram_permalink_url). |  [optional] |
|**instagramAccountId** | **String** | Instagram-only. The connected Instagram SocialAccount these comments were read through — use it for reply/hide actions via /v1/inbox/comments. |  [optional] |
|**accountId** | **String** | Social account ID (ads SocialAccount). |  |
|**lastUpdated** | **OffsetDateTime** |  |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



