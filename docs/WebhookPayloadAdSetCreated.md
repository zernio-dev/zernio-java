

# WebhookPayloadAdSetCreated

Webhook payload for the `ad_set.created` event. Fires when an ad set is created through Zernio (API, MCP or dashboard), once per ad set, after its row is recorded so `GET /v1/ads/ad-sets/{adSetId}` finds it.  History loaded when an account connects is never announced.  An ad set is announced at most once per 24 hours. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookAdsAccount**](WebhookAdsAccount.md) |  |  |
|**adObject** | [**WebhookPayloadAdSetCreatedAdObject**](WebhookPayloadAdSetCreatedAdObject.md) |  |  |
|**source** | [**SourceEnum**](#SourceEnum) | Where the ad set was created. &#x60;zernio&#x60; for ad sets created through Zernio. |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| AD_SET_CREATED | &quot;ad_set.created&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| ZERNIO | &quot;zernio&quot; |
| PLATFORM | &quot;platform&quot; |



