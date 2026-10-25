

# ListTikTokSmartPlusReviews200ResponseItemsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**smartPlusAdId** | **String** |  |  [optional] |
|**adGroupId** | **String** |  |  [optional] |
|**campaignId** | **String** |  |  [optional] |
|**review** | [**TikTokSmartPlusAdLevelReview**](TikTokSmartPlusAdLevelReview.md) |  |  [optional] |
|**materials** | [**List&lt;TikTokSmartPlusMaterialReview&gt;**](TikTokSmartPlusMaterialReview.md) | One entry per creative TikTok reviewed (&#x60;material_review_infos&#x60;). |  [optional] |
|**readAt** | **OffsetDateTime** | When the verdict was read from TikTok, kept as is when served from the store. Older than &#x60;maxAgeSeconds&#x60; means stale. |  [optional] |



