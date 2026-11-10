

# CreatorCampaign


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**userId** | **String** | The workspace billing owner the campaign belongs to. |  |
|**profileId** | **String** | The profile that scopes the campaign: API keys, teammates and webhooks scoped to it reach the campaign. |  |
|**kind** | **String** |  |  |
|**name** | **String** |  |  |
|**brandName** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | draft until activated; active accepts submissions and accrues; paused stops new submissions; closed is final. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Same as economics.type. |  |
|**currency** | **String** |  |  |
|**platforms** | [**List&lt;PlatformsEnum&gt;**](#List&lt;PlatformsEnum&gt;) |  |  |
|**contentRules** | **String** | Free-text rules shown to creators on the join page. |  |
|**startsAt** | **OffsetDateTime** |  |  |
|**endsAt** | **OffsetDateTime** | No new submissions after this time; the campaign closes once every tracking window had its final read. |  |
|**trackingDays** | **Integer** | How long each submitted post is tracked. |  |
|**holdDays** | **Integer** | Days approved earnings are held before they become payable. |  |
|**maxPostAgeMinutes** | **Integer** | A post older than this many minutes when submitted is refused. Null (the default) accepts any age. Either way, a post published before the campaign started (&#x60;startsAt&#x60;, or &#x60;activatedAt&#x60; without one) is refused. |  |
|**activatedAt** | **OffsetDateTime** | When the campaign was first activated. Without &#x60;startsAt&#x60;, posts must be published after this moment. |  |
|**settlement** | [**SettlementEnum**](#SettlementEnum) | none: settle records a payout made elsewhere. external: you pay from your own rails on campaign_payout.payable and settle with your reference. treasury: you pay by card with a payout batch and Zernio pays each creator in your name 7 days after the charge. |  |
|**economics** | [**CreatorCampaignEconomics**](CreatorCampaignEconomics.md) |  |  |
|**caps** | [**CreatorCampaignCaps**](CreatorCampaignCaps.md) |  |  |
|**branding** | [**CreatorCampaignBranding**](CreatorCampaignBranding.md) |  |  |
|**budgetExhaustedAt** | **OffsetDateTime** |  |  |
|**closedAt** | **OffsetDateTime** |  |  |
|**payableScannedAt** | **OffsetDateTime** | Internal watermark of the payable scan. |  |
|**joinApproval** | [**JoinApprovalEnum**](#JoinApprovalEnum) | auto: creators who join through the open link are active at once. manual: they land &#x60;pending&#x60; until you approve or deny them. Personal invites are never held. |  |
|**requireDraftApproval** | **Boolean** | Creators upload a draft for review first, and submit the live post for an approved draft (&#x60;draftId&#x60;). |  |
|**storeAccountId** | **String** | The connected store (Shopify or WooCommerce) whose orders pay commission and whose products creators can ask as samples. Null when the campaign has neither. |  |
|**sampleProducts** | [**List&lt;CreatorCampaignSampleProduct&gt;**](CreatorCampaignSampleProduct.md) | Products creators can ask a free sample of. |  |
|**sampleContentDueDays** | **Integer** | Days after a sample is approved before a creator with no post since shows as owing content (&#x60;contentOwed&#x60;). |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**hasOpenInvite** | **Boolean** | True once an open invite link was created. The link itself is returned only when it is created. |  |
|**consumedCents** | **Integer** | Budget used so far: earnings accrued, approved or adjusted against the campaign. |  |
|**participantCount** | **Integer** |  |  |
|**submissionCounts** | [**CampaignSubmissionCounts**](CampaignSubmissionCounts.md) |  |  |
|**payableCents** | **Integer** | What the campaign&#39;s creators can be paid now, summed over every participant&#39;s payable balance. |  |
|**landingUrl** | **String** | The page creator tracking links open. |  [optional] |
|**codeDiscountPercent** | **Integer** | What each creator discount code takes off. |  [optional] |
|**pendingParticipantCount** | **Integer** | Creators who asked to join through the open link and wait for a decision. Not counted in &#x60;participantCount&#x60;. |  |
|**draftCounts** | [**CampaignDraftCounts**](CampaignDraftCounts.md) |  |  |
|**sampleCounts** | [**CampaignSampleCounts**](CampaignSampleCounts.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |
| CLOSED | &quot;closed&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CPM | &quot;cpm&quot; |
| PER_POST | &quot;per_post&quot; |
| POOL | &quot;pool&quot; |
| RETAINER | &quot;retainer&quot; |
| COMMISSION | &quot;commission&quot; |
| AD_PERFORMANCE | &quot;ad_performance&quot; |



## Enum: List&lt;PlatformsEnum&gt;

| Name | Value |
|---- | -----|
| TIKTOK | &quot;tiktok&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| YOUTUBE | &quot;youtube&quot; |
| THREADS | &quot;threads&quot; |
| PINTEREST | &quot;pinterest&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TWITTER | &quot;twitter&quot; |



## Enum: SettlementEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| EXTERNAL | &quot;external&quot; |
| TREASURY | &quot;treasury&quot; |



## Enum: JoinApprovalEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| MANUAL | &quot;manual&quot; |



