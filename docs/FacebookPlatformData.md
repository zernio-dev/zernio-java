

# FacebookPlatformData

Facebook post settings.  - Feed posts: up to 10 images (no mixed video+image). - Stories: single media (24h, no captions). - Reels: a single vertical video (9:16). The Zernio API does not preflight Reel duration; Meta's Reels publishing guide documents 3-90 seconds. - Geo-restriction: a hard visibility restriction (users outside the specified countries cannot see the post). Not supported for stories.  Draft, carousel and colored-background text options live under facebookSettings, see FacebookSettings. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | Set to &#39;story&#39; for Page Stories (24h ephemeral) or &#39;reel&#39; for Reels (short vertical video). Defaults to feed post if omitted. |  [optional] |
|**title** | **String** | Reel title (only for contentType&#x3D;reel). Separate from the caption/content field. |  [optional] |
|**firstComment** | **String** | Optional first comment to post immediately after publishing (feed posts and reels, not stories). Skipped when facebookSettings.draft is true. |  [optional] |
|**isAiGenerated** | **Boolean** | When true, Facebook shows its AI-disclosure label on the post. Forwarded as is_ai_generated on Reels (contentType&#x3D;reel) and video Stories (contentType&#x3D;story with a video). Meta documents no such parameter for feed posts, feed videos or photo Stories, so the flag is accepted with a warning and no label there. |  [optional] |
|**pageId** | **String** | Target Facebook Page ID for multi-page posting. If omitted, uses the default page. Use GET /v1/accounts/{id}/facebook-page to list pages. |  [optional] |
|**geoRestriction** | [**GeoRestriction**](GeoRestriction.md) |  |  [optional] |
|**collaborators** | **List&lt;String&gt;** | Facebook Page IDs (numeric, up to 10 unique) to invite as collaborators. Reels only (contentType&#x3D;reel), sent after the Reel is published, never for drafts. Each Page must accept. Meta allows 10 invites per Page per 24 hours; rejected invites are listed in failedCollaborators. Other values are ignored with a warning. |  [optional] |
|**failedCollaborators** | [**List&lt;FacebookPlatformDataFailedCollaboratorsInner&gt;**](FacebookPlatformDataFailedCollaboratorsInner.md) | Output only. Collaborator invites Facebook rejected after the Reel was published. The Reel itself stays published. |  [optional] |
|**facebookSettings** | [**FacebookSettings**](FacebookSettings.md) |  |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| STORY | &quot;story&quot; |
| REEL | &quot;reel&quot; |



