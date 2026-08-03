

# UpdatePostRequestPlatformsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** |  |  |
|**accountId** | **String** |  |  |
|**customContent** | **String** | Platform-specific text override. |  [optional] |
|**customMedia** | [**List&lt;MediaItem&gt;**](MediaItem.md) |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** | Optional per-platform scheduled time override. |  [optional] |
|**platformSpecificData** | **Map&lt;String, Object&gt;** | A &lt;platform&gt;Settings namespace (e.g. facebookSettings, tiktokSettings) omitted from the request is preserved from the stored post. Sending the key replaces the whole namespace; it is not deep-merged. |  [optional] |



