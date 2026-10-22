

# TikTokSmartPlusAdLevelReview

The ad-level verdict of a Smart+ ad (`smart_plus_ad_review_infos`). Null when TikTok returned none.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reviewStatus** | **TikTokSmartPlusReviewStatus** |  |  [optional] |
|**rawReviewStatus** | **String** | TikTok &#x60;review_status&#x60;, verbatim. |  [optional] |
|**rejectReasons** | **List&lt;String&gt;** | Every distinct reason across &#x60;rejections&#x60;. |  [optional] |
|**passedLocations** | **List&lt;String&gt;** | Location codes that passed the review. |  [optional] |
|**appealStatus** | **String** | TikTok &#x60;appeal_status&#x60;, verbatim: NOT_APPEALED, APPEALING, APPEAL_SUCCESSFUL, APPEAL_FAILED, APPEAL_DONE. |  [optional] |
|**appealRejectReasons** | **List&lt;String&gt;** |  |  [optional] |
|**rejections** | [**List&lt;TikTokReviewRejection&gt;**](TikTokReviewRejection.md) |  |  [optional] |



