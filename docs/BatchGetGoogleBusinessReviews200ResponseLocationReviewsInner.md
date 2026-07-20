

# BatchGetGoogleBusinessReviews200ResponseLocationReviewsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | LOCATION resource name the review belongs to (accounts/{accountId}/locations/{locationId}) - NOT the review resource name. Use it to attribute the review to a location; the review identity is review.reviewId (full review resource name at review.name). |  [optional] |
|**review** | **Object** | The review object: reviewId (the review&#39;s identity), name (full review resource name, accounts/_*_/locations/_*_/reviews/_*), starRating, comment, reviewer, createTime, updateTime, reviewReply, and reviewMediaItems (review photos/videos; photo items carry thumbnailUrl, video items carry videoUrl) |  [optional] |



