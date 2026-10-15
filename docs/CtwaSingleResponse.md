

# CtwaSingleResponse

Response returned by `POST /v1/ads/ctwa` when the request used the single-creative shape (top-level headline / body / imageUrl|video). `adType` is the union discriminator. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adType** | [**AdTypeEnum**](#AdTypeEnum) |  |  |
|**ad** | **Object** | The persisted Ad document. |  |
|**message** | **String** |  |  |
|**warnings** | **List&lt;String&gt;** | Present when Meta created the ad set differently from the request: Meta kept the ad set without the requested &#x60;whatsappPhoneNumber&#x60; in its promoted_object (the ads still carry it on their WhatsApp button), or the ad set joined a CBO campaign (&#x60;existingCampaignId&#x60;) whose own bid strategy applies, so a different &#x60;bidStrategy&#x60; or a &#x60;roasAverageFloor&#x60; that strategy cannot take was not applied. |  [optional] |



## Enum: AdTypeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |



