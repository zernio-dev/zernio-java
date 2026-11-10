

# CampaignSample

A free product sample a creator asked for.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**campaignId** | **String** |  |  |
|**participantId** | **String** |  |  |
|**creator** | [**CreatorCampaignAdResultsSubmissionsInnerCreator**](CreatorCampaignAdResultsSubmissionsInnerCreator.md) |  |  |
|**storeAccountId** | **String** | The store the sample comes from. |  |
|**productId** | **String** |  |  |
|**variantId** | **String** |  |  |
|**productTitle** | **String** |  |  |
|**variantTitle** | **String** |  |  |
|**shippingAddress** | [**CampaignSampleShippingAddress**](CampaignSampleShippingAddress.md) |  |  |
|**note** | **String** | The creator&#39;s note. |  |
|**status** | [**StatusEnum**](#StatusEnum) | pending: waits for review. approved: a discount code was created. shipped: you recorded that you sent it. declined: final for this request. |  |
|**declineReason** | **String** |  |  |
|**discountCode** | **String** | The 100%-off, single-use code for the product, set on approval. |  |
|**trackingUrl** | **String** |  |  |
|**approvedAt** | **OffsetDateTime** |  |  |
|**shippedAt** | **OffsetDateTime** |  |  |
|**requestedAt** | **OffsetDateTime** |  |  |
|**contentDueAt** | **OffsetDateTime** | When a post is due: the approval plus the campaign&#39;s &#x60;sampleContentDueDays&#x60;. Null unless approved or shipped. |  |
|**contentOwed** | **Boolean** | True past &#x60;contentDueAt&#x60; when the creator submitted no post since the approval. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| SHIPPED | &quot;shipped&quot; |
| DECLINED | &quot;declined&quot; |



