

# WebhookPayloadReviewNew

Webhook payload for the `review.new` event (new review posted on a connected account).

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
| REVIEW_NEW | &quot;review.new&quot; |



