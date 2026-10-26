

# AdTracking

Meta, plus `urlTags` on ChatGPT (OpenAI) and `pixelId` on Reddit. Meta: attaches pixel measurement to the ad regardless of the optimization goal (the \"Website events\" tracking row in Ads Manager). `pixelId` becomes the ad's `tracking_specs` (offsite_conversion + fb_pixel); `urlTags` is stored on the new creative as `url_tags` and retained on the ad for compatibility. Applied on the legacy single-creative shape, every ad of the multi-creative shape, and the attach shape. NOTE: tracking lives on the AD object and is not inherited from the ad set, so pass it on EVERY attach call that should carry the pixel. ChatGPT (OpenAI): `urlTags` becomes the ad's `landing_page_configuration.query_string_template`, which OpenAI appends to `linkUrl` on click. Reddit: `pixelId` picks the pixel of the new ad group, like `promotedObject.pixelId` (which wins when both are sent).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** | Meta Pixel ID to attach for offsite-conversion measurement, or the Reddit pixel of the new ad group. |  [optional] |
|**urlTags** | [**List&lt;UpdateAdTrackingTagsRequestUrlTagsInner&gt;**](UpdateAdTrackingTagsRequestUrlTagsInner.md) | Click-URL params. Meta: stored on the creative as &#x60;url_tags&#x60; and returned by GET /v1/ads/{adId}/tracking-tags. App-promotion linkUrl stays byte-identical to promotedObject.objectStoreUrl. Meta dynamic macros ({{ad.id}}, {{campaign.id}}, {{placement}}, ...) are sent through unescaped so Meta expands them; every other character is percent-encoded. ChatGPT (OpenAI): the same encoding, with OpenAI&#39;s macros &#x60;{campaign_id}&#x60;, &#x60;{ad_group_id}&#x60;, &#x60;{ad_id}&#x60; and &#x60;{oppref}&#x60; (click id) passed through raw. OpenAI expands macros here, not inside &#x60;linkUrl&#x60;. |  [optional] |
|**zernioTag** | **Boolean** | POST /v1/ads/create on Meta and Google only. Every ad created there carries &#x60;zrn&#x3D;&lt;platform ad id&gt;&#x60; on its landing URL so orders and events tied to the landing URL map back to the ad. Meta: &#x60;{ key: zrn, value: &#39;{{ad.id}}&#39; }&#x60; is appended after your &#x60;urlTags&#x60;, which are sent unchanged; a &#x60;zrn&#x60; key you send yourself is kept. Skipped for lead forms, call ads, &#x60;existingCreativeId&#x60; and app promotion. Google (Display and Search): the ad&#39;s &#x60;final_url_suffix&#x60; becomes the suffix it would inherit (ad group, campaign or account) plus &#x60;&amp;zrn&#x3D;{creative}&#x60;, so your account and campaign UTMs still apply; if that suffix cannot be read or Google rejects it, the ad is created untagged. Existing ads are never changed. Set &#x60;false&#x60; to create the ad with no Zernio tag. |  [optional] |



