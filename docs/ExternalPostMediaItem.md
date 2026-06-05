

# ExternalPostMediaItem

A media item on a native (external/synced) post, as carried by post.external.* webhook payloads. Distinct from the richer MediaItem used for Zernio-authored posts: external items are always already-published (url required) and limited to image or video. Kept as a separate schema so the generated SDK model does not collide with MediaItem. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**url** | **String** |  |  |
|**thumbnail** | **String** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |



