

# WebhookPayloadComment

Webhook payload for comment received events (Instagram, Facebook, Threads, YouTube, LinkedIn, Bluesky, Reddit, TikTok). X/Twitter does NOT fire this event. TikTok events carry only the author id: the comment.update webhook has no username, picture or owner flag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**comment** | [**WebhookPayloadCommentComment**](WebhookPayloadCommentComment.md) |  |  |
|**post** | [**WebhookPayloadCommentPost**](WebhookPayloadCommentPost.md) |  |  |
|**account** | [**WebhookPayloadCommentAccount**](WebhookPayloadCommentAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| COMMENT_RECEIVED | &quot;comment.received&quot; |



