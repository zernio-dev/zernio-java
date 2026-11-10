

# CampaignDraft

One version of a creator's content, uploaded for review before it is published. A revision is a new version in the same `chainId` with `version` + 1 and `revisionOf` set to the version it answers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**campaignId** | **String** |  |  |
|**participantId** | **String** |  |  |
|**creator** | [**CreatorCampaignAdResultsSubmissionsInnerCreator**](CreatorCampaignAdResultsSubmissionsInnerCreator.md) |  |  |
|**chainId** | **String** | The id of the first version of the chain. |  |
|**version** | **Integer** |  |  |
|**revisionOf** | **String** | The version this one answers; null on version 1. |  |
|**mediaUrl** | **URI** |  |  |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  |
|**caption** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | submitted: waits for review. approved: the creator may publish it. revision_requested: the creator should upload a new version. rejected: final. |  |
|**reviewNote** | **String** | The note sent with a revision request, or the rejection reason. |  |
|**reviewedAt** | **OffsetDateTime** |  |  |
|**submittedAt** | **OffsetDateTime** |  |  |
|**comments** | [**List&lt;CampaignDraftCommentsInner&gt;**](CampaignDraftCommentsInner.md) | Review comments on this version, in video order. |  |
|**submissionId** | **String** | The live post submitted for this draft, once the creator published it. |  |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| VIDEO | &quot;video&quot; |
| IMAGE | &quot;image&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;submitted&quot; |
| APPROVED | &quot;approved&quot; |
| REVISION_REQUESTED | &quot;revision_requested&quot; |
| REJECTED | &quot;rejected&quot; |



