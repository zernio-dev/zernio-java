

# WebhookPayloadCampaignStatusChanged

Webhook payload for the `campaign.status_changed` event. Fires when the ads sync sees a campaign Zernio already tracked change its platform status or, on Google, its status reasons.  `status` carries the platform's own values: Google's `primary_status` (`ELIGIBLE`, `LIMITED`, `NOT_ELIGIBLE`, `PAUSED`, ...), the campaign's own status on every other network (Meta `effective_status`: `ACTIVE`, `PAUSED`, `WITH_ISSUES`, ...).  Never fires for a campaign seen for the first time. The same change (same previous and new status and reasons) fires at most once per campaign per hour. A change made through Zernio fires on the next sync. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookAdsAccount**](WebhookAdsAccount.md) |  |  |
|**campaign** | [**WebhookPayloadCampaignStatusChangedCampaign**](WebhookPayloadCampaignStatusChangedCampaign.md) |  |  |
|**platform** | **String** | The ad network, as the ads endpoints name it (&#x60;google&#x60;, &#x60;facebook&#x60;, &#x60;tiktok&#x60;, ...). |  |
|**adAccountId** | **String** | Platform-native ad account ID. |  |
|**status** | [**WebhookPayloadCampaignStatusChangedStatus**](WebhookPayloadCampaignStatusChangedStatus.md) |  |  |
|**reasons** | [**WebhookPayloadCampaignStatusChangedReasons**](WebhookPayloadCampaignStatusChangedReasons.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CAMPAIGN_STATUS_CHANGED | &quot;campaign.status_changed&quot; |



