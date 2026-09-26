

# AdTracking

Meta, plus `urlTags` on ChatGPT (OpenAI). Meta: attaches pixel measurement to the ad regardless of the optimization goal (the \"Website events\" tracking row in Ads Manager). `pixelId` becomes the ad's `tracking_specs` (offsite_conversion + fb_pixel); `urlTags` is stored on the new creative as `url_tags` and retained on the ad for compatibility. Applied on the legacy single-creative shape, every ad of the multi-creative shape, and the attach shape. NOTE: tracking lives on the AD object and is not inherited from the ad set, so pass it on EVERY attach call that should carry the pixel. ChatGPT (OpenAI): `urlTags` becomes the ad's `landing_page_configuration.query_string_template`, which OpenAI appends to `linkUrl` on click.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** | Meta Pixel ID to attach for offsite-conversion measurement. |  [optional] |
|**urlTags** | [**List&lt;UpdateAdTrackingTagsRequestUrlTagsInner&gt;**](UpdateAdTrackingTagsRequestUrlTagsInner.md) | Click-URL params. Meta: stored on the creative as &#x60;url_tags&#x60; and returned by GET /v1/ads/{adId}/tracking-tags. App-promotion linkUrl stays byte-identical to promotedObject.objectStoreUrl. Meta dynamic macros ({{ad.id}}, {{campaign.id}}, {{placement}}, ...) are sent through unescaped so Meta expands them; every other character is percent-encoded. ChatGPT (OpenAI): the same encoding, with OpenAI&#39;s macros &#x60;{campaign_id}&#x60;, &#x60;{ad_group_id}&#x60;, &#x60;{ad_id}&#x60; and &#x60;{oppref}&#x60; (click id) passed through raw. OpenAI expands macros here, not inside &#x60;linkUrl&#x60;. |  [optional] |



