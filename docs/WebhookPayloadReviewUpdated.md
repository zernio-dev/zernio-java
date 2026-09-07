

# WebhookPayloadReviewUpdated

Webhook payload for the review.updated event. Fired when the reviewer edits their text or rating, or when a reply is posted through POST /v1/inbox/reviews/{reviewId}/reply. A reply written directly in Google's own interface does NOT fire this event: Google emits no notification when a reviewReply is written. Same shape as review.new. When a reply is present, review.hasReply is true and review.reply is populated. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**review** | [**ReviewWebhookReview**](ReviewWebhookReview.md) |  |  |
|**account** | [**WebhookPayloadReviewNewAccount**](WebhookPayloadReviewNewAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| REVIEW_UPDATED | &quot;review.updated&quot; |



