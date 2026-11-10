

# CreatorPortalDraft

One version of a draft the creator uploaded for review.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Pass as &#x60;draftId&#x60; when submitting the live post of an approved draft, or as &#x60;revisionOf&#x60; to answer a revision request. |  |
|**chainId** | **String** |  |  |
|**version** | **Integer** |  |  |
|**revisionOf** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**mediaUrl** | **URI** |  |  |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  |
|**caption** | **String** |  |  |
|**reviewNote** | **String** |  |  |
|**comments** | [**List&lt;CreatorPortalDraftCommentsInner&gt;**](CreatorPortalDraftCommentsInner.md) |  |  |
|**submittedAt** | **OffsetDateTime** |  |  |
|**reviewedAt** | **OffsetDateTime** |  |  |
|**submissionId** | **String** | The live post submitted for this draft. |  |



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



