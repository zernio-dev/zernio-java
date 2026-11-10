

# CreatorPortalSample


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**productId** | **String** |  |  |
|**productTitle** | **String** |  |  |
|**variantTitle** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**shippingAddress** | [**CampaignSampleShippingAddress**](CampaignSampleShippingAddress.md) |  |  |
|**note** | **String** |  |  |
|**discountCode** | **String** | The single-use code to redeem the product at checkout, once approved. |  |
|**trackingUrl** | **String** |  |  |
|**declineReason** | **String** |  |  |
|**requestedAt** | **OffsetDateTime** |  |  |
|**contentDueAt** | **OffsetDateTime** | When a post is due for the sample; null until approved. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| SHIPPED | &quot;shipped&quot; |
| DECLINED | &quot;declined&quot; |



