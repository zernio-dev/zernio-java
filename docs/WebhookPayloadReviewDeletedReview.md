

# WebhookPayloadReviewDeletedReview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Full review name, matching review.id on the review.new event (\&quot;accounts/123/locations/456/reviews/789\&quot;). |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**rating** | **Integer** | Star rating the reviewer gave. Null when it was never recorded. |  |
|**createdAt** | **OffsetDateTime** | When the reviewer posted the review. Null when it was never recorded. |  |
|**lastSeenAt** | **OffsetDateTime** | Last time Zernio saw Google return this review. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLEBUSINESS | &quot;googlebusiness&quot; |



