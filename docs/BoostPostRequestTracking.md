

# BoostPostRequestTracking

Meta only. Tracking specs (pixel, URL tags).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** |  |  [optional] |
|**urlTags** | [**List&lt;BoostPostRequestTrackingUrlTagsInner&gt;**](BoostPostRequestTrackingUrlTagsInner.md) | URL parameters appended to the ad link, rendered as &#x60;key&#x3D;value&#x60; pairs joined with &#x60;&amp;&#x60;. Meta dynamic macros ({{ad.id}}, {{campaign.id}}, {{placement}}, ...) are sent through unescaped so Meta expands them; every other character is percent-encoded. |  [optional] |



