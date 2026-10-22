

# GetTikTokSmartPlusAdReview200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**platformAdId** | **String** |  |  [optional] |
|**smartPlusAdId** | **String** | The TikTok Smart+ ad whose review this is. |  [optional] |
|**review** | [**TikTokSmartPlusAdLevelReview**](TikTokSmartPlusAdLevelReview.md) |  |  [optional] |
|**materials** | [**List&lt;TikTokSmartPlusMaterialReview&gt;**](TikTokSmartPlusMaterialReview.md) | One entry per creative TikTok reviewed (&#x60;material_review_infos&#x60;). |  [optional] |
|**readAt** | **OffsetDateTime** | When the verdict was read from TikTok. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| TIKTOK | &quot;tiktok&quot; |



