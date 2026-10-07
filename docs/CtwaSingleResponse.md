

# CtwaSingleResponse

Response returned by `POST /v1/ads/ctwa` when the request used the single-creative shape (top-level headline / body / imageUrl|video). `adType` is the union discriminator. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adType** | [**AdTypeEnum**](#AdTypeEnum) |  |  |
|**ad** | **Object** | The persisted Ad document. |  |
|**message** | **String** |  |  |
|**warnings** | **List&lt;String&gt;** | Present when Meta created the ad set differently from the request. Today: Meta kept the ad set without the requested &#x60;whatsappPhoneNumber&#x60; in its promoted_object (the ads still carry it on their WhatsApp button). |  [optional] |



## Enum: AdTypeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |



