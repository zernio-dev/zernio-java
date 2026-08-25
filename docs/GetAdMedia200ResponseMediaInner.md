

# GetAdMedia200ResponseMediaInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**url** | **String** | Direct file URL (signed; short-lived — see description). |  [optional] |
|**thumbnailUrl** | **String** | Video poster URL (videos only). |  [optional] |
|**videoId** | **String** | Meta video id (videos only), reusable as video.id on the create endpoints. |  [optional] |
|**length** | **BigDecimal** | Video length in seconds (videos only). |  [optional] |
|**index** | **Integer** | 0-based position for carousel children or asset_feed_spec entries. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |



