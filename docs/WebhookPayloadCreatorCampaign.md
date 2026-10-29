

# WebhookPayloadCreatorCampaign

Webhook payload for `creator_campaign.budget_exhausted` and `creator_campaign.closed`. `budget_exhausted` fires once, when the campaign's earnings first reach `campaign.budgetCents`, and carries `campaign.budgetExhaustedAt`. `closed` fires once, when the campaign closes, and carries `campaign.closedAt`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**campaign** | [**WebhookPayloadCreatorCampaignCampaign**](WebhookPayloadCreatorCampaignCampaign.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CREATOR_CAMPAIGN_BUDGET_EXHAUSTED | &quot;creator_campaign.budget_exhausted&quot; |
| CREATOR_CAMPAIGN_CLOSED | &quot;creator_campaign.closed&quot; |



