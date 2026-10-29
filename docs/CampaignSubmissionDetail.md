

# CampaignSubmissionDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**campaignId** | **String** |  |  |
|**participantId** | **String** |  |  |
|**creatorId** | **String** |  |  |
|**accountId** | **String** | The creator account the post was published from. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**platformPostId** | **String** |  |  |
|**platformPostUrl** | **String** |  |  |
|**externalPostId** | **String** | The tracked external post (see /v1/external-posts). |  |
|**trackingWindowId** | **String** |  |  |
|**mediaHash** | **String** |  |  |
|**submittedAt** | **OffsetDateTime** |  |  |
|**postPublishedAt** | **OffsetDateTime** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**rejectReason** | **String** |  |  |
|**reviewRound** | **Integer** | How many times the post was reopened after a reject. 0 until the first reopen. |  |
|**reviewedBy** | **String** | User id of the reviewer. |  |
|**reviewedAt** | **OffsetDateTime** |  |  |
|**viewsAtSubmission** | **Integer** | Views when the post was submitted. They count toward earnings like every later view. |  |
|**viewsLatest** | **Integer** | Latest view count read for the post, frozen at the tracking window end. |  |
|**viewsEligible** | **Integer** | Views that count toward earnings: every view the platform reports for the post, including those before submission, read at the tracking window end at the latest: once the window completes or is cancelled, the last read at or before its end is final and this value stops moving. |  |
|**lastAccruedViews** | **Integer** |  |  |
|**accruedCents** | **Integer** |  |  |
|**approvedCents** | **Integer** |  |  |
|**authenticityScore** | **Integer** |  |  |
|**authenticityConfidence** | **BigDecimal** |  |  |
|**flags** | [**List&lt;CampaignSubmissionFlag&gt;**](CampaignSubmissionFlag.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**creator** | [**WebhookPayloadCampaignSubmissionCreator**](WebhookPayloadCampaignSubmissionCreator.md) |  |  |
|**authenticity** | [**CampaignSubmissionAuthenticity**](CampaignSubmissionAuthenticity.md) |  |  |
|**earnedCents** | **Integer** | approvedCents once approved, otherwise accruedCents. |  |
|**releasedCents** | **Integer** | Approved cents whose hold is over, so payable or already paid out. 0 unless approved. |  |
|**paidOutCents** | **Integer** | What rejecting this post could not take back now: releasedCents beyond the creator&#39;s payable balance. It stays paid; the dashboard warns before such a reject. |  |
|**window** | [**CampaignSubmissionWindow**](CampaignSubmissionWindow.md) |  |  |
|**post** | [**CampaignSubmissionPost**](CampaignSubmissionPost.md) |  |  |
|**samples** | [**List&lt;CampaignSubmissionDetailAllOfSamples&gt;**](CampaignSubmissionDetailAllOfSamples.md) | Counters per sync, newest first, up to 500. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| TIKTOK | &quot;tiktok&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| YOUTUBE | &quot;youtube&quot; |
| THREADS | &quot;threads&quot; |
| PINTEREST | &quot;pinterest&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TWITTER | &quot;twitter&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RECEIVED | &quot;received&quot; |
| TRACKING | &quot;tracking&quot; |
| PENDING_REVIEW | &quot;pending_review&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |
| EXPIRED | &quot;expired&quot; |
| WITHDRAWN | &quot;withdrawn&quot; |



