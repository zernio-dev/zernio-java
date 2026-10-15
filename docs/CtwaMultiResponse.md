

# CtwaMultiResponse

Response returned by `POST /v1/ads/ctwa` when the request used the multi-creative shape (`creatives[]`). N persisted Ad documents share the returned `platformCampaignId` and `platformAdSetId`. `adType` is the union discriminator. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adType** | [**AdTypeEnum**](#AdTypeEnum) |  |  |
|**ads** | **List&lt;Object&gt;** | The persisted Ad documents (one per creative), all sharing the same &#x60;platformCampaignId&#x60; and &#x60;platformAdSetId&#x60;.  |  |
|**platformCampaignId** | **String** |  |  |
|**platformAdSetId** | **String** |  |  |
|**message** | **String** |  |  |
|**warnings** | **List&lt;String&gt;** | Present when Meta created the ad set differently from the request: Meta kept the ad set without the requested &#x60;whatsappPhoneNumber&#x60; in its promoted_object (the ads still carry it on their WhatsApp button), or the ad set joined a CBO campaign (&#x60;existingCampaignId&#x60;) whose own bid strategy applies, so a different &#x60;bidStrategy&#x60; or a &#x60;roasAverageFloor&#x60; that strategy cannot take was not applied. |  [optional] |



## Enum: AdTypeEnum

| Name | Value |
|---- | -----|
| MULTI | &quot;multi&quot; |



