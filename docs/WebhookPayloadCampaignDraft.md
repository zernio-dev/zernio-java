

# WebhookPayloadCampaignDraft

Webhook payload for `campaign_draft.submitted`, `campaign_draft.approved`, `campaign_draft.revision_requested` and `campaign_draft.rejected`. `draft` is the version the event is about; `draft.status` is its status after the change. 

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
|**draft** | [**WebhookPayloadCampaignDraftDraft**](WebhookPayloadCampaignDraftDraft.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CAMPAIGN_DRAFT_SUBMITTED | &quot;campaign_draft.submitted&quot; |
| CAMPAIGN_DRAFT_APPROVED | &quot;campaign_draft.approved&quot; |
| CAMPAIGN_DRAFT_REVISION_REQUESTED | &quot;campaign_draft.revision_requested&quot; |
| CAMPAIGN_DRAFT_REJECTED | &quot;campaign_draft.rejected&quot; |



