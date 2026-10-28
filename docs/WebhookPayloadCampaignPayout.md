

# WebhookPayloadCampaignPayout

Webhook payload for `campaign_payout.payable` and `campaign_payout.settled`. `payable` fires when a participant's held earnings mature; `payout.payableCents` is the participant's whole payable balance, so a partner paying from its own rails pays that amount and records it with `POST /v1/creator-campaigns/{campaignId}/participants/{participantId}/settle`. `settled` fires when a settlement is recorded and carries `payout.settlement`. `failed` fires when a treasury payout is refused, unconfirmed or reversed; the amount returns to payable (minus anything a rejection claws back) and `payout.failure` says why. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Present on every event tied to a profile and absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once. Use it to route the event to your tenant without storing Zernio profile ids. |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**campaign** | [**WebhookPayloadCampaignPayoutCampaign**](WebhookPayloadCampaignPayoutCampaign.md) |  |  |
|**participant** | [**WebhookPayloadCampaignSubmissionParticipant**](WebhookPayloadCampaignSubmissionParticipant.md) |  |  |
|**creator** | [**WebhookPayloadCampaignSubmissionCreator**](WebhookPayloadCampaignSubmissionCreator.md) |  |  |
|**payout** | [**WebhookPayloadCampaignPayoutPayout**](WebhookPayloadCampaignPayoutPayout.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CAMPAIGN_PAYOUT_PAYABLE | &quot;campaign_payout.payable&quot; |
| CAMPAIGN_PAYOUT_SETTLED | &quot;campaign_payout.settled&quot; |
| CAMPAIGN_PAYOUT_FAILED | &quot;campaign_payout.failed&quot; |



