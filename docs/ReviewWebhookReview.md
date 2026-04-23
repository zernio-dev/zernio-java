

# ReviewWebhookReview

Review data shared by review.new and review.updated payloads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform review ID (e.g. \&quot;accounts/123/locations/456/reviews/789\&quot; for Google Business). |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform the review originated on. Currently Google Business Profile only. |  |
|**rating** | **Integer** | Star rating the reviewer gave. |  |
|**text** | **String** | Review text content. May be empty if the reviewer left only a rating. |  |
|**reviewer** | [**ReviewWebhookReviewReviewer**](ReviewWebhookReviewReviewer.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**hasReply** | **Boolean** | Whether the connected account has replied to this review. |  |
|**reply** | [**ReviewWebhookReviewReply**](ReviewWebhookReviewReply.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLEBUSINESS | &quot;googlebusiness&quot; |



