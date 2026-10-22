

# PrepareMedia200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**target** | **String** |  |  |
|**url** | **URI** | URL to publish: the prepared file, or the input URL when nothing needed to change. |  |
|**changed** | **Boolean** | Whether the media was processed. |  |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  |
|**originalSize** | **Integer** | Input size in bytes, null when the host does not report it. |  |
|**outputSize** | **Integer** | Size of the returned file in bytes. |  |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |



