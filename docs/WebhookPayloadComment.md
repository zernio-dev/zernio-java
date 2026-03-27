

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
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| COMMENT_RECEIVED | &quot;comment.received&quot; |



