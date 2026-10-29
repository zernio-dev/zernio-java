

# WebhookPayloadAnalyticsSynced

Webhook payload for `analytics.synced`. Fired once per connected account each time its analytics sync cycle completes successfully. Poll-driven (roughly hourly per account), not real-time, and never fired for a skipped or failed cycle.  A TRIGGER, not a transport: it deliberately carries no metrics and no cursor. When it arrives, call `GET /v1/analytics/delta` with YOUR OWN last `nextCursor` to read what changed, across every account, in one paginated stream.  **Why there is no cursor.** The feed's ordering position is assigned inside the analytics store when the row is materialized, which normally happens after this event fires. A cursor minted here could sit ahead of the rows the event announces and make you skip them. Your own `nextCursor` never can.  Because of the same lag, a delta read issued the instant this event lands can legitimately come back empty. That is not \"nothing changed\": poll again with the same cursor you last used rather than treating the account as done.  **Use a DEDICATED webhook endpoint.** This event is high volume (roughly one delivery per connected account per hour), and a subscription's consecutive-failure count is shared across all its events. An outage while it flows can suppress the low-volume publishing events on the same subscription. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadAnalyticsSyncedAccount**](WebhookPayloadAnalyticsSyncedAccount.md) |  |  |
|**sync** | [**WebhookPayloadAnalyticsSyncedSync**](WebhookPayloadAnalyticsSyncedSync.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| ANALYTICS_SYNCED | &quot;analytics.synced&quot; |



