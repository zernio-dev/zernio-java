

# WebhookPayloadReviewDeletedReview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Google: full review name. Facebook: the review id from review.new. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**rating** | **Integer** | Star rating the reviewer gave. Null when it was never recorded. |  |
|**createdAt** | **OffsetDateTime** | When the reviewer posted the review. Null when it was never recorded. Always null on Facebook. |  |
|**lastSeenAt** | **OffsetDateTime** | Last time Zernio saw Google return this review. On Facebook, when Meta&#39;s removal notice arrived. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLEBUSINESS | &quot;googlebusiness&quot; |
| FACEBOOK | &quot;facebook&quot; |



