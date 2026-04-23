

# WebhookPayloadReviewUpdated

Webhook payload for the review.updated event. Fired when the reviewer edits their text or rating, or when a reply is added (via the API or directly on the platform). Same shape as review.new. When a reply is present, review.hasReply is true and review.reply is populated. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**review** | [**ReviewWebhookReview**](ReviewWebhookReview.md) |  |  |
|**account** | [**WebhookPayloadReviewNewAccount**](WebhookPayloadReviewNewAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| REVIEW_UPDATED | &quot;review.updated&quot; |



