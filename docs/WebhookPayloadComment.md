

# WebhookPayloadComment

Webhook payload for comment received events (Instagram, Facebook, Twitter/X, YouTube, LinkedIn, Bluesky, Reddit)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**comment** | [**WebhookPayloadCommentComment**](WebhookPayloadCommentComment.md) |  |  |
|**post** | [**WebhookPayloadCommentPost**](WebhookPayloadCommentPost.md) |  |  |
|**account** | [**WebhookPayloadCommentAccount**](WebhookPayloadCommentAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| COMMENT_RECEIVED | &quot;comment.received&quot; |



