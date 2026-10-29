

# WebhookPayloadCampaignSubmission

Webhook payload for campaign submission events:  - `campaign_submission.received`: fires for every accepted submission. - `campaign_submission.flagged`: fires when a submission gains a flag it did not carry before (at submission or on a later sync). `submission.flags` lists every flag it carries. - `campaign_submission.pending_review`: fires when the submission becomes ready for the operator's review. - `campaign_submission.approved` and `campaign_submission.rejected`: fire on the operator's decision. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**campaign** | [**UpdateAdRequestTargetingInterestsInner**](UpdateAdRequestTargetingInterestsInner.md) |  |  |
|**participant** | [**WebhookPayloadCampaignSubmissionParticipant**](WebhookPayloadCampaignSubmissionParticipant.md) |  |  |
|**creator** | [**WebhookPayloadCampaignSubmissionCreator**](WebhookPayloadCampaignSubmissionCreator.md) |  |  |
|**submission** | [**WebhookPayloadCampaignSubmissionSubmission**](WebhookPayloadCampaignSubmissionSubmission.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CAMPAIGN_SUBMISSION_RECEIVED | &quot;campaign_submission.received&quot; |
| CAMPAIGN_SUBMISSION_FLAGGED | &quot;campaign_submission.flagged&quot; |
| CAMPAIGN_SUBMISSION_PENDING_REVIEW | &quot;campaign_submission.pending_review&quot; |
| CAMPAIGN_SUBMISSION_APPROVED | &quot;campaign_submission.approved&quot; |
| CAMPAIGN_SUBMISSION_REJECTED | &quot;campaign_submission.rejected&quot; |



