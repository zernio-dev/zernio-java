

# CtwaSingleResponse

Response returned by `POST /v1/ads/ctwa` when the request used the single-creative shape (top-level headline / body / imageUrl|video). `adType` is the union discriminator. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adType** | [**AdTypeEnum**](#AdTypeEnum) |  |  |
|**ad** | **Object** | The persisted Ad document. |  |
|**message** | **String** |  |  |



## Enum: AdTypeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |



