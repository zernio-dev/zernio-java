

# CreateStandaloneAdRequestTracking

Meta only. Attaches pixel measurement to the ad regardless of the optimization goal (the \"Website events\" tracking row in Ads Manager). `pixelId` becomes the ad's `tracking_specs` (offsite_conversion + fb_pixel); `urlTags` becomes the ad's `url_tags` (click-tracking query params). Applied to every ad on the legacy single-creative and multi-creative shapes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** | Meta Pixel ID to attach for offsite-conversion measurement. |  [optional] |
|**urlTags** | [**List&lt;UpdateAdTrackingTagsRequestUrlTagsInner&gt;**](UpdateAdTrackingTagsRequestUrlTagsInner.md) | Click-URL params appended to the ad&#39;s destination as &#x60;url_tags&#x60; (e.g. utm_source). |  [optional] |



