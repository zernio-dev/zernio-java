

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
|**warnings** | **List&lt;String&gt;** | Present when Meta created the ad set differently from the request. Today: Meta kept the ad set without the requested &#x60;whatsappPhoneNumber&#x60; in its promoted_object (the ads still carry it on their WhatsApp button). |  [optional] |



## Enum: AdTypeEnum

| Name | Value |
|---- | -----|
| MULTI | &quot;multi&quot; |



