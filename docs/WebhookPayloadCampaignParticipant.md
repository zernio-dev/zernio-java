

# WebhookPayloadCampaignParticipant

Webhook payload for `campaign_participant.joined`, `campaign_participant.suspended` and `campaign_participant.removed`. `participant.status` is the status after the change. `participant.joinedAt` is null for a participant removed before they ever joined. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Present on every event tied to a profile and absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once. Use it to route the event to your tenant without storing Zernio profile ids. |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**campaign** | [**UpdateAdRequestTargetingInterestsInner**](UpdateAdRequestTargetingInterestsInner.md) |  |  |
|**participant** | [**WebhookPayloadCampaignParticipantParticipant**](WebhookPayloadCampaignParticipantParticipant.md) |  |  |
|**creator** | [**WebhookPayloadCampaignSubmissionCreator**](WebhookPayloadCampaignSubmissionCreator.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CAMPAIGN_PARTICIPANT_JOINED | &quot;campaign_participant.joined&quot; |
| CAMPAIGN_PARTICIPANT_SUSPENDED | &quot;campaign_participant.suspended&quot; |
| CAMPAIGN_PARTICIPANT_REMOVED | &quot;campaign_participant.removed&quot; |



