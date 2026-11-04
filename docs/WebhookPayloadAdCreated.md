

# WebhookPayloadAdCreated

Webhook payload for the `ad.created` event. Fires when an ad is created through Zernio (API, MCP or dashboard) or detected by the sync, once per ad, after its campaign and ad set are recorded so `GET /v1/ads/{adId}` finds them.  `source` is `zernio` for ads created through Zernio and `platform` for ads our sync detected, up to one sync interval later (Meta ads entering review usually arrive within minutes). History loaded when an account connects, and ads created more than 7 days ago, are never announced.  An ad is announced at most once per 24 hours. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookAdsAccount**](WebhookAdsAccount.md) |  |  |
|**adObject** | [**WebhookPayloadAdCreatedAdObject**](WebhookPayloadAdCreatedAdObject.md) |  |  |
|**source** | [**SourceEnum**](#SourceEnum) | Where the ad was created. &#x60;zernio&#x60; for ads created through Zernio, &#x60;platform&#x60; for ads the sync detected. |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| AD_CREATED | &quot;ad.created&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| ZERNIO | &quot;zernio&quot; |
| PLATFORM | &quot;platform&quot; |



