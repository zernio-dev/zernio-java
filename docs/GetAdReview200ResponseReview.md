

# GetAdReview200ResponseReview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approved** | **Boolean** | TikTok &#x60;is_approved&#x60;. Google and Meta: derived from the platform status (see the description). |  [optional] |
|**reviewStatus** | **String** | TikTok &#x60;review_status&#x60;, verbatim: ALL_AVAILABLE (approved everywhere), PART_AVAILABLE (approved for part of the targeting), UNAVAILABLE (rejected). Google: &#x60;review_status&#x60;. Meta: the ad&#39;s &#x60;effective_status&#x60;. |  [optional] |
|**forbiddenPlacements** | **List&lt;String&gt;** |  |  [optional] |
|**forbiddenAges** | **List&lt;String&gt;** |  |  [optional] |
|**forbiddenLocations** | **List&lt;String&gt;** |  |  [optional] |
|**forbiddenOperatingSystems** | **List&lt;String&gt;** |  |  [optional] |
|**rejections** | [**List&lt;GetAdReview200ResponseReviewRejectionsInner&gt;**](GetAdReview200ResponseReviewRejectionsInner.md) | One entry per rejected piece of content (TikTok &#x60;reject_info&#x60;). Empty when the ad was approved. |  [optional] |
|**approvalStatus** | **String** | Google only. ad_group_ad.policy_summary.approval_status, verbatim. |  [optional] |
|**policyTopics** | [**List&lt;GetAdReview200ResponseReviewPolicyTopicsInner&gt;**](GetAdReview200ResponseReviewPolicyTopicsInner.md) | Google only. ad_group_ad.policy_summary.policy_topic_entries. |  [optional] |
|**reviewFeedback** | [**GetAdReview200ResponseReviewReviewFeedback**](GetAdReview200ResponseReviewReviewFeedback.md) |  |  [optional] |
|**issues** | **List&lt;Object&gt;** | Meta only. The Ad&#39;s &#x60;issues_info&#x60; objects (&#x60;error_code&#x60;, &#x60;error_message&#x60;, &#x60;error_summary&#x60;, &#x60;error_type&#x60;, &#x60;level&#x60;), verbatim. |  [optional] |
|**readAt** | **OffsetDateTime** | When the verdict was read from the platform. |  [optional] |



