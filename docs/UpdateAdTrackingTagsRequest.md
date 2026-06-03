

# UpdateAdTrackingTagsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**urlTags** | [**List&lt;UpdateAdTrackingTagsRequestUrlTagsInner&gt;**](UpdateAdTrackingTagsRequestUrlTagsInner.md) | Meta only. Click-URL params appended to a freshly-rebuilt creative. |  [optional] |
|**creative** | [**UpdateAdTrackingTagsRequestCreative**](UpdateAdTrackingTagsRequestCreative.md) |  |  [optional] |
|**trackingUrlTemplate** | **String** | Google only. Full tracking template (must contain {lpurl}). |  [optional] |
|**finalUrlSuffix** | **String** | Google only. Parse-only key&#x3D;value params. |  [optional] |
|**dynamicValueParameters** | **Map&lt;String, String&gt;** | LinkedIn only. key -&gt; dynamic value enum (CAMPAIGN_ID, CAMPAIGN_NAME, CREATIVE_ID, ...). |  [optional] |
|**customValueParameters** | **Map&lt;String, String&gt;** | LinkedIn only. key -&gt; static value. |  [optional] |



