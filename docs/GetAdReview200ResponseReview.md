

# GetAdReview200ResponseReview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approved** | **Boolean** | TikTok &#x60;is_approved&#x60;. |  [optional] |
|**reviewStatus** | **String** | TikTok &#x60;review_status&#x60;, verbatim: ALL_AVAILABLE (approved everywhere), PART_AVAILABLE (approved for part of the targeting), UNAVAILABLE (rejected). |  [optional] |
|**forbiddenPlacements** | **List&lt;String&gt;** |  |  [optional] |
|**forbiddenAges** | **List&lt;String&gt;** |  |  [optional] |
|**forbiddenLocations** | **List&lt;String&gt;** |  |  [optional] |
|**forbiddenOperatingSystems** | **List&lt;String&gt;** |  |  [optional] |
|**rejections** | [**List&lt;GetAdReview200ResponseReviewRejectionsInner&gt;**](GetAdReview200ResponseReviewRejectionsInner.md) | One entry per rejected piece of content (TikTok &#x60;reject_info&#x60;). Empty when the ad was approved. |  [optional] |
|**approvalStatus** | **String** | Google only. ad_group_ad.policy_summary.approval_status, verbatim. |  [optional] |
|**policyTopics** | [**List&lt;GetAdReview200ResponseReviewPolicyTopicsInner&gt;**](GetAdReview200ResponseReviewPolicyTopicsInner.md) | Google only. ad_group_ad.policy_summary.policy_topic_entries. |  [optional] |
|**readAt** | **OffsetDateTime** | When the verdict was read from the platform. |  [optional] |



