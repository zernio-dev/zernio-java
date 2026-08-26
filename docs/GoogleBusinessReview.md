

# GoogleBusinessReview

A Google Business Profile review, as returned by every gmb-reviews read endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Review ID |  [optional] |
|**name** | **String** | Full resource name |  [optional] |
|**reviewer** | [**GoogleBusinessReviewReviewer**](GoogleBusinessReviewReviewer.md) |  |  [optional] |
|**rating** | **Integer** | Numeric star rating (0 when Google sends no rating) |  [optional] |
|**starRating** | [**StarRatingEnum**](#StarRatingEnum) | Google&#39;s string rating |  [optional] |
|**comment** | **String** | Review text |  [optional] |
|**createTime** | **OffsetDateTime** |  |  [optional] |
|**updateTime** | **OffsetDateTime** |  |  [optional] |
|**reviewReply** | [**GoogleBusinessReviewReviewReply**](GoogleBusinessReviewReviewReply.md) |  |  [optional] |
|**photoCount** | **Integer** | Number of photos attached to the review (photos only, videos are not counted) |  [optional] |
|**photos** | [**List&lt;ListInboxReviews200ResponseDataInnerPhotosInner&gt;**](ListInboxReviews200ResponseDataInnerPhotosInner.md) | Photos attached to the review by the reviewer |  [optional] |



## Enum: StarRatingEnum

| Name | Value |
|---- | -----|
| ONE | &quot;ONE&quot; |
| TWO | &quot;TWO&quot; |
| THREE | &quot;THREE&quot; |
| FOUR | &quot;FOUR&quot; |
| FIVE | &quot;FIVE&quot; |



