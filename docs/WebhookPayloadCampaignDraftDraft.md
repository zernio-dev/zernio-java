

# WebhookPayloadCampaignDraftDraft


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**chainId** | **String** |  |  |
|**version** | **Integer** |  |  |
|**revisionOf** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**mediaUrl** | **String** |  |  |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  |
|**caption** | **String** |  |  |
|**reviewNote** | **String** | The revision note or the rejection reason. |  |
|**comments** | [**List&lt;CreatorPortalDraftCommentsInner&gt;**](CreatorPortalDraftCommentsInner.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;submitted&quot; |
| APPROVED | &quot;approved&quot; |
| REVISION_REQUESTED | &quot;revision_requested&quot; |
| REJECTED | &quot;rejected&quot; |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| VIDEO | &quot;video&quot; |
| IMAGE | &quot;image&quot; |



