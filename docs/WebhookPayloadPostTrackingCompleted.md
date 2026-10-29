

# WebhookPayloadPostTrackingCompleted

Webhook payload for `post.tracking_completed`. Fired once when a post's tracking window ends and its final analytics read has run.  `final` holds the closing metrics, or null when no sample could be read.  `window.completionReason` says how the window closed:  - `final_read`: the read succeeded. - `unreachable`: the sync failed or no sample exists. - `post_deleted`: the post is gone from the platform; `final` is then the last sample we held, if any. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**post** | [**WebhookPayloadPostTrackingCompletedPost**](WebhookPayloadPostTrackingCompletedPost.md) |  |  |
|**window** | [**WebhookPayloadPostTrackingCompletedWindow**](WebhookPayloadPostTrackingCompletedWindow.md) |  |  |
|**_final** | [**WebhookPayloadPostTrackingCompletedFinal**](WebhookPayloadPostTrackingCompletedFinal.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| POST_TRACKING_COMPLETED | &quot;post.tracking_completed&quot; |



