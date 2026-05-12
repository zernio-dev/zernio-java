

# GetAdComments200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) | Which side these comments are on (same as &#x60;placement&#x60;). |  |
|**placement** | [**PlacementEnum**](#PlacementEnum) | The placement these comments are for — useful when you didn&#39;t pass ?placement&#x3D; and want to know which one you got. |  |
|**adId** | **String** | Internal Zernio ad ID. |  |
|**platformAdId** | **String** | Meta ad ID. |  |
|**effectiveStoryId** | **String** | Underlying post ID the comments belong to. effective_object_story_id for the Facebook side, effective_instagram_media_id for the Instagram side. |  |
|**facebookAccountId** | **String** | Facebook-only. The connected Facebook Page SocialAccount these comments were read through — pass it as &#x60;accountId&#x60; (with &#x60;effectiveStoryId&#x60; as the postId) to /v1/inbox/comments to reply/hide/delete. Null when no connected Page was used (then moderation isn&#39;t possible). |  [optional] |
|**instagramUserId** | **String** | Instagram-only. The Instagram-scoped business ID that owns the boosted media (creative.instagram_user_id). |  [optional] |
|**instagramPermalink** | **String** | Instagram-only. Public permalink of the boosted IG post (creative.instagram_permalink_url). |  [optional] |
|**instagramAccountId** | **String** | Instagram-only. The connected Instagram SocialAccount these comments were read through — pass it as &#x60;accountId&#x60; (with &#x60;effectiveStoryId&#x60; as the postId) to /v1/inbox/comments to reply/hide/delete. |  [optional] |
|**accountId** | **String** | Social account ID (ads SocialAccount). |  |
|**lastUpdated** | **OffsetDateTime** |  |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



## Enum: PlacementEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



