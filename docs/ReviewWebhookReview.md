

# ReviewWebhookReview

Review data shared by review.new, review.updated and review.restored payloads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform review ID (e.g. \&quot;accounts/123/locations/456/reviews/789\&quot; for Google Business Profile). |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform the review originated on (Google Business Profile or Facebook Pages). |  |
|**rating** | **Integer** | Star rating the reviewer gave. Null for a Facebook recommendation without stars. |  |
|**recommendationType** | [**RecommendationTypeEnum**](#RecommendationTypeEnum) | Facebook only. Whether the reviewer recommended the Page. |  [optional] |
|**text** | **String** | Review text content. May be empty if the reviewer left only a rating. |  |
|**reviewer** | [**ReviewWebhookReviewReviewer**](ReviewWebhookReviewReviewer.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**hasReply** | **Boolean** | Whether the connected account has replied to this review. |  |
|**reply** | [**ReviewWebhookReviewReply**](ReviewWebhookReviewReply.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLEBUSINESS | &quot;googlebusiness&quot; |
| FACEBOOK | &quot;facebook&quot; |



## Enum: RecommendationTypeEnum

| Name | Value |
|---- | -----|
| POSITIVE | &quot;positive&quot; |
| NEGATIVE | &quot;negative&quot; |



