

# GetAdComments200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform of the comments. |  |
|**placement** | [**PlacementEnum**](#PlacementEnum) | The placement these comments are for, useful when you didn&#39;t pass ?placement&#x3D; and want to know which one you got. |  [optional] |
|**adId** | **String** | Internal Zernio ad ID. |  |
|**platformAdId** | **String** | Platform ad ID. |  [optional] |
|**effectiveStoryId** | **String** | Underlying post ID the comments belong to. effective_object_story_id for the Facebook side, effective_instagram_media_id for the Instagram side. |  [optional] |
|**tiktokItemId** | **String** | TikTok-only video item ID. Null when the ad and comments do not expose it. |  [optional] |
|**since** | **LocalDate** | TikTok-only resolved start date. |  [optional] |
|**until** | **LocalDate** | TikTok-only resolved end date. |  [optional] |
|**facebookAccountId** | **String** | Facebook-only. The connected Facebook Page SocialAccount these comments were read through. Pass it as &#x60;accountId&#x60; (with &#x60;effectiveStoryId&#x60; as the postId) to /v1/inbox/comments to reply/hide/delete. Null when no connected Page was used (then moderation isn&#39;t possible). |  [optional] |
|**instagramUserId** | **String** | Instagram-only. The Instagram-scoped business ID that owns the boosted media (creative.instagram_user_id). |  [optional] |
|**instagramPermalink** | **String** | Instagram-only. Public permalink of the boosted IG post (creative.instagram_permalink_url). |  [optional] |
|**instagramAccountId** | **String** | Instagram-only. The connected Instagram SocialAccount these comments were read through. Pass it as &#x60;accountId&#x60; (with &#x60;effectiveStoryId&#x60; as the postId) to /v1/inbox/comments to reply/hide/delete. |  [optional] |
|**accountId** | **String** | Account ID (ads SocialAccount). |  |
|**lastUpdated** | **OffsetDateTime** |  |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| TIKTOK | &quot;tiktok&quot; |



## Enum: PlacementEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



