

# FacebookPlatformData

Feed posts support up to 10 images (no mixed video+image). Stories require single media (24h, no captions). Reels require single vertical video (9:16, 3-60s). Geo-restriction is a hard visibility restriction: users outside the specified countries cannot see the post. Not supported for stories. Draft, carousel, and colored-background text options live under facebookSettings, see FacebookSettings. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | Set to &#39;story&#39; for Page Stories (24h ephemeral) or &#39;reel&#39; for Reels (short vertical video). Defaults to feed post if omitted. |  [optional] |
|**title** | **String** | Reel title (only for contentType&#x3D;reel). Separate from the caption/content field. |  [optional] |
|**firstComment** | **String** | Optional first comment to post immediately after publishing (feed posts and reels, not stories). Skipped when facebookSettings.draft is true. |  [optional] |
|**pageId** | **String** | Target Facebook Page ID for multi-page posting. If omitted, uses the default page. Use GET /v1/accounts/{id}/facebook-page to list pages. |  [optional] |
|**geoRestriction** | [**GeoRestriction**](GeoRestriction.md) |  |  [optional] |
|**facebookSettings** | [**FacebookSettings**](FacebookSettings.md) |  |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| STORY | &quot;story&quot; |
| REEL | &quot;reel&quot; |



