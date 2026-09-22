

# ListInboxReviews200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Review identifier. For Google Business Profile this is the full review resource name (accounts/{accountId}/locations/{locationId}/reviews/{reviewId}), so it also encodes the location. |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**locationId** | **String** | Bare Google Business Profile location id the review belongs to. Google Business Profile only; absent for other platforms. |  [optional] |
|**locationName** | **String** | Human-readable Google Business Profile location display name. Google Business Profile only; absent for other platforms. |  [optional] |
|**reviewer** | [**ListInboxReviews200ResponseDataInnerReviewer**](ListInboxReviews200ResponseDataInnerReviewer.md) |  |  [optional] |
|**rating** | **Integer** |  |  [optional] |
|**recommendationType** | [**RecommendationTypeEnum**](#RecommendationTypeEnum) | Facebook recommendation: positive means recommends, negative means does not recommend. Null or absent when unavailable; absent for other platforms. Independent of the numeric rating. |  [optional] |
|**text** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] |
|**hasReply** | **Boolean** |  |  [optional] |
|**hasPhotos** | **Boolean** | Whether the review has at least one photo. Google Business Profile only; always false for other platforms. |  [optional] |
|**photoCount** | **Integer** | Number of photos attached to the review (photos only; videos are not counted). Google Business Profile only; 0 for other platforms. |  [optional] |
|**photos** | [**List&lt;ListInboxReviews200ResponseDataInnerPhotosInner&gt;**](ListInboxReviews200ResponseDataInnerPhotosInner.md) | Photos attached to the review. Google Business Profile only; always an empty array for other platforms. |  [optional] |
|**reply** | [**ListInboxReviews200ResponseDataInnerReply**](ListInboxReviews200ResponseDataInnerReply.md) |  |  [optional] |
|**reviewUrl** | **String** |  |  [optional] |



## Enum: RecommendationTypeEnum

| Name | Value |
|---- | -----|
| POSITIVE | &quot;positive&quot; |
| NEGATIVE | &quot;negative&quot; |



