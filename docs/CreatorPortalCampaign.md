

# CreatorPortalCampaign

The campaign as a creator sees it: terms, never the budget.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The campaign id, as in a link-recovery URL. |  |
|**name** | **String** |  |  |
|**brandName** | **String** |  |  |
|**logoUrl** | **String** |  |  |
|**theme** | **Object** | Same keys as the &#x60;welcomeTheme&#x60; parameter of &#x60;GET /v1/connect/{platform}&#x60;. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**platforms** | **List&lt;String&gt;** |  |  |
|**contentRules** | **String** |  |  |
|**startsAt** | **OffsetDateTime** |  |  |
|**endsAt** | **OffsetDateTime** |  |  |
|**startedAt** | **OffsetDateTime** | Posts published before this moment do not count: &#x60;startsAt&#x60;, else when the campaign went live. |  |
|**currency** | **String** |  |  |
|**economics** | [**CreatorPortalEconomics**](CreatorPortalEconomics.md) |  |  |
|**maxPostAgeMinutes** | **Integer** | A post must be submitted within this many minutes of publishing. Null means any age. Either way, only posts published after the campaign started are accepted. |  |
|**holdDays** | **Integer** | Days approved earnings stay owed before they become payable. |  |
|**trackingDays** | **Integer** | Days each submitted post is tracked for views. |  |
|**maxAccountsPerParticipant** | **Integer** | How many connected accounts can submit posts. Null means no limit. |  |
|**joinApproval** | [**JoinApprovalEnum**](#JoinApprovalEnum) | manual: a creator who joins through the open link waits &#x60;pending&#x60; until the campaign team accepts them. |  |
|**requireDraftApproval** | **Boolean** | The creator uploads a draft for review first, and submits the live post for an approved draft. |  |
|**sampleProducts** | [**List&lt;CreatorCampaignSampleProduct&gt;**](CreatorCampaignSampleProduct.md) | Products the creator can ask a free sample of; empty when the campaign offers none. |  |
|**sampleContentDueDays** | **Integer** | Days after a sample is approved by which a post is expected. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |
| CLOSED | &quot;closed&quot; |



## Enum: JoinApprovalEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| MANUAL | &quot;manual&quot; |



