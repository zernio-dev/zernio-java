

# GoogleAdsUserAccessInvitationResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** |  |  [optional] |
|**emailAddress** | **String** |  |  [optional] |
|**accessRole** | **GoogleAdsAccessRole** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | PENDING once the email is sent; PENDING_APPROVAL while Google waits for a second admin&#39;s multi-party approval. |  [optional] |
|**invitationId** | **String** | Null on validateOnly and while the invitation awaits multi-party approval. |  [optional] |
|**multiPartyAuthReviewId** | **String** | Google&#39;s multi-party approval review id when status is PENDING_APPROVAL. |  [optional] |
|**validateOnly** | **Boolean** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| PENDING_APPROVAL | &quot;PENDING_APPROVAL&quot; |



