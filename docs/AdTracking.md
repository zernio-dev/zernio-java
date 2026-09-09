

# AdTracking

Meta only. Attaches pixel measurement to the ad regardless of the optimization goal (the \"Website events\" tracking row in Ads Manager). `pixelId` becomes the ad's `tracking_specs` (offsite_conversion + fb_pixel); `urlTags` is stored on the new creative as `url_tags` and retained on the ad for compatibility. Applied on the legacy single-creative shape, every ad of the multi-creative shape, and the attach shape. NOTE: tracking lives on the AD object and is not inherited from the ad set, so pass it on EVERY attach call that should carry the pixel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** | Meta Pixel ID to attach for offsite-conversion measurement. |  [optional] |
|**urlTags** | [**List&lt;UpdateAdTrackingTagsRequestUrlTagsInner&gt;**](UpdateAdTrackingTagsRequestUrlTagsInner.md) | Click-URL params stored on the creative as &#x60;url_tags&#x60; and returned by GET /v1/ads/{adId}/tracking-tags. App-promotion linkUrl stays byte-identical to promotedObject.objectStoreUrl. Meta dynamic macros ({{ad.id}}, {{campaign.id}}, {{placement}}, ...) are sent through unescaped so Meta expands them; every other character is percent-encoded. |  [optional] |



