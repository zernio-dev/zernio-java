

# WebhookPayloadPostPlatform

Webhook payload for these per-platform events:  - `post.platform.published` and `post.platform.failed`: terminal events. - `post.platform.deleted`: same shape, fired when Zernio's background sync detects that a platform target published through Zernio was later deleted on the platform (poll-driven ~hourly, not real-time). - `post.tiktok.url_resolved`: same shape, fired when a published TikTok post's public URL is backfilled.  Terminal events fire once per platform target inside a post as that platform reaches a terminal state (published or permanent failure). Exception: a target that later fails background reconciliation emits `post.platform.failed` a second time, after its own `post.platform.published`.  **Blocks**: the `post` envelope mirrors `WebhookPayloadPost` so consumers can reuse rendering logic; `platform` identifies which specific platform transitioned; `account` identifies the connected account behind that platform-write. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**post** | [**WebhookPayloadPostPlatformPost**](WebhookPayloadPostPlatformPost.md) |  |  |
|**platform** | [**WebhookPayloadPostPlatformPlatform**](WebhookPayloadPostPlatformPlatform.md) |  |  |
|**account** | [**WebhookPayloadPostPlatformAccount**](WebhookPayloadPostPlatformAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| POST_PLATFORM_PUBLISHED | &quot;post.platform.published&quot; |
| POST_PLATFORM_FAILED | &quot;post.platform.failed&quot; |
| POST_PLATFORM_DELETED | &quot;post.platform.deleted&quot; |
| POST_TIKTOK_URL_RESOLVED | &quot;post.tiktok.url_resolved&quot; |



