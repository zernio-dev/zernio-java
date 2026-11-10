

# WebhookPayloadCampaignSampleSample


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**storeAccountId** | **String** |  |  |
|**productId** | **String** |  |  |
|**variantId** | **String** |  |  |
|**productTitle** | **String** |  |  |
|**variantTitle** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**shippingAddress** | [**CampaignSampleShippingAddress**](CampaignSampleShippingAddress.md) |  |  |
|**note** | **String** |  |  |
|**discountCode** | **String** | The 100%-off, single-use code, set from approval on. |  |
|**trackingUrl** | **String** |  |  |
|**declineReason** | **String** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| SHIPPED | &quot;shipped&quot; |
| DECLINED | &quot;declined&quot; |



