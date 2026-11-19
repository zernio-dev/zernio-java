

# GetAdReview200ResponseReviewAssetGroup

Google Performance Max only. The asset group's serving status and each linked asset's policy review.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**primaryStatus** | **String** | asset_group.primary_status, verbatim: ELIGIBLE, LIMITED, NOT_ELIGIBLE, PAUSED, PENDING, REMOVED. |  |
|**primaryStatusReasons** | **List&lt;String&gt;** | asset_group.primary_status_reasons, verbatim, such as ASSET_GROUP_DISAPPROVED, ASSET_GROUP_UNDER_REVIEW, ASSET_GROUP_LIMITED, CAMPAIGN_PAUSED. Empty when the group serves without issues. |  |
|**assets** | [**List&lt;GetAdReview200ResponseReviewAssetGroupAssetsInner&gt;**](GetAdReview200ResponseReviewAssetGroupAssetsInner.md) |  |  |



