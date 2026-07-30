

# FacebookPlatformData

Feed posts support up to 10 images (no mixed video+image). Stories require single media (24h, no captions). Reels require single vertical video (9:16, 3-60s). Carousel posts (carouselCards) render a 2-5 card multi-link post, images only, mutually exclusive with story/reel. Geo-restriction is a hard visibility restriction: users outside the specified countries cannot see the post. Not supported for stories. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**draft** | **Boolean** | When true, creates the post as a draft in Facebook Publishing Tools instead of publishing immediately. Supported for feed posts (text, link, image, video) and reels. Not supported for stories. Drafts expire after ~30 days. |  [optional] |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | Set to &#39;story&#39; for Page Stories (24h ephemeral) or &#39;reel&#39; for Reels (short vertical video). Defaults to feed post if omitted. |  [optional] |
|**title** | **String** | Reel title (only for contentType&#x3D;reel). Separate from the caption/content field. |  [optional] |
|**firstComment** | **String** | Optional first comment to post immediately after publishing (feed posts and reels, not stories). Skipped when draft is true. |  [optional] |
|**pageId** | **String** | Target Facebook Page ID for multi-page posting. If omitted, uses the default page. Use GET /v1/accounts/{id}/facebook-page to list pages. |  [optional] |
|**geoRestriction** | [**GeoRestriction**](GeoRestriction.md) |  |  [optional] |
|**carouselCards** | [**List&lt;FacebookPlatformDataCarouselCardsInner&gt;**](FacebookPlatformDataCarouselCardsInner.md) | Renders the post as a multi-link carousel (organic Page post). When set, mediaItems must be provided with the same length and all items must be images (no videos). Each cards[i] adds the click-through link and headline for the image at mediaItems[i]. Mutually exclusive with contentType&#x3D;story|reel. Facebook display truncates name at ~35 chars and description at ~30 chars; longer strings are accepted but get truncated on render.  |  [optional] |
|**carouselLink** | **URI** | Optional top-level \&quot;See more\&quot; destination shown on the carousel end card. Defaults to the first card&#39;s link when omitted. Only used together with carouselCards.  |  [optional] |
|**textFormatPresetId** | **String** | Facebook-defined preset ID that renders the post as large text on a colored background (Graph &#x60;text_format_preset_id&#x60;). Supply the raw numeric ID from Meta; we do not publish a catalog of presets and Facebook may change the available set. Pages only (ignored on personal profiles and groups) and text-only feed posts only: the request is rejected with 400 when mediaItems or carouselCards are present, when contentType is story or reel, when content is empty, or when content exceeds 130 characters. Those are Facebook limits, and above them Facebook silently drops the background and publishes a plain text post instead of returning an error, so we reject up front rather than let the background disappear. A URL detected in the content is NOT attached as a link preview while a preset is set, because a link attachment also makes Facebook drop the background.  |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| STORY | &quot;story&quot; |
| REEL | &quot;reel&quot; |



