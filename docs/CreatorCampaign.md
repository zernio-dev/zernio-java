

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
|**settlement** | [**SettlementEnum**](#SettlementEnum) | none: settle records a payout made elsewhere. external: you pay from your own rails on campaign_payout.payable and settle with your reference. treasury: settle moves the money from your Zernio balance to the creator&#39;s Stripe account, and the creator sets up payouts from their campaign page. |  |
|**economics** | [**CreatorCampaignEconomics**](CreatorCampaignEconomics.md) |  |  |
|**caps** | [**CreatorCampaignCaps**](CreatorCampaignCaps.md) |  |  |
|**branding** | [**CreatorCampaignBranding**](CreatorCampaignBranding.md) |  |  |
|**budgetExhaustedAt** | **OffsetDateTime** |  |  |
|**closedAt** | **OffsetDateTime** |  |  |
|**payableScannedAt** | **OffsetDateTime** | Internal watermark of the payable scan. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**hasOpenInvite** | **Boolean** | True once an open invite link was created. The link itself is returned only when it is created. |  |
|**consumedCents** | **Integer** | Budget used so far: earnings accrued, approved or adjusted against the campaign. |  |
|**participantCount** | **Integer** |  |  |
|**submissionCounts** | [**CampaignSubmissionCounts**](CampaignSubmissionCounts.md) |  |  |
|**payableCents** | **Integer** | What the campaign&#39;s creators can be paid now, summed over every participant&#39;s payable balance. |  |



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



