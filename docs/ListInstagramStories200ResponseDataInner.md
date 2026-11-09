

# ListInstagramStories200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Instagram media ID of the story. |  |
|**mediaType** | **String** | IMAGE / VIDEO / CAROUSEL_ALBUM |  [optional] |
|**mediaProductType** | **String** | Always &#39;STORY&#39; for this endpoint. |  [optional] |
|**mediaUrl** | **String** | Direct media URL. Null if Meta flagged the story for copyright. URL expires when the story expires. |  [optional] |
|**permalink** | **String** | Public Instagram permalink to the story (only viewable while live). |  [optional] |
|**thumbnailUrl** | **String** | Thumbnail URL for video stories. |  [optional] |
|**timestamp** | **OffsetDateTime** | When the story was posted. |  [optional] |
|**expired** | **Boolean** | Only with &#x60;includeExpired&#x3D;true&#x60;. True for an archived story that is no longer live; its media urls point to Zernio storage. |  [optional] |
|**metrics** | [**ListInstagramStories200ResponseDataInnerMetrics**](ListInstagramStories200ResponseDataInnerMetrics.md) |  |  [optional] |



