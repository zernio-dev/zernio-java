

# WebhookPayloadConversationStarted

Fired once when a new conversation begins, in either direction. A conversation starts the first time an account and a contact exchange a message on any DM platform (Instagram, Messenger/Facebook, Telegram, WhatsApp, X, Reddit, Bluesky, SMS, TikTok). Platform-agnostic: one subscription covers every DM platform.  `conversation.metadata` (the referral as Meta sent it) and `conversation.adAttribution` (the ad, campaign and ad set from your synced ads) are filled only when the message that created the conversation carried Meta's referral. That holds for WhatsApp Click-to-WhatsApp and Facebook Messenger Click-to-Message, and for ig.me / m.me ref links. On Instagram Click-to-Direct it usually does NOT: Meta creates the thread with the ad post itself, an attachment-only `share` / `ig_post` message with no referral, and attaches the referral to the next message. That conversation.started then has `adAttribution` null and no `metadata`. Read the click from `metadata.ad` and `metadata.referral` on the `message.received` that follows, or from `adAttribution` on `GET /v1/inbox/conversations` and `GET /v1/inbox/conversations/{conversationId}`, which carry it once the referral is stored. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Present on every event tied to a profile and absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once. Use it to route the event to your tenant without storing Zernio profile ids. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**conversation** | [**WebhookPayloadConversationStartedConversation**](WebhookPayloadConversationStartedConversation.md) |  |  |
|**account** | [**InboxWebhookAccount**](InboxWebhookAccount.md) |  |  |
|**startedAt** | **OffsetDateTime** | When the conversation document was created. |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CONVERSATION_STARTED | &quot;conversation.started&quot; |



