

# ListInboxReviews200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**reviewer** | [**ListInboxReviews200ResponseDataInnerReviewer**](ListInboxReviews200ResponseDataInnerReviewer.md) |  |  [optional] |
|**rating** | **Integer** |  |  [optional] |
|**text** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] |
|**hasReply** | **Boolean** |  |  [optional] |
|**hasPhotos** | **Boolean** | Whether the review has at least one photo. Google Business only; always false for other platforms. |  [optional] |
|**photoCount** | **Integer** | Number of photos attached to the review (photos only; videos are not counted). Google Business only; 0 for other platforms. |  [optional] |
|**photos** | [**List&lt;GetGoogleBusinessReviews200ResponseReviewsInnerPhotosInner&gt;**](GetGoogleBusinessReviews200ResponseReviewsInnerPhotosInner.md) | Photos attached to the review. Google Business only; always an empty array for other platforms. |  [optional] |
|**reply** | [**ListInboxReviews200ResponseDataInnerReply**](ListInboxReviews200ResponseDataInnerReply.md) |  |  [optional] |
|**reviewUrl** | **String** |  |  [optional] |



