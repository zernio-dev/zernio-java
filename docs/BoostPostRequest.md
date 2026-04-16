

# BoostPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postId** | **String** | Zernio post ID (provide this or platformPostId) |  [optional] |
|**platformPostId** | **String** | Platform post ID (alternative to postId) |  [optional] |
|**accountId** | **String** | Social account ID |  |
|**adAccountId** | **String** | Platform ad account ID |  |
|**name** | **String** |  |  |
|**goal** | [**GoalEnum**](#GoalEnum) | Available goals vary by platform. Meta (Facebook/Instagram) and TikTok support all 7. LinkedIn supports all except app_promotion. Twitter/X supports engagement, traffic, awareness, video_views, app_promotion. Pinterest and Google Ads support only engagement, traffic, awareness, video_views. |  |
|**budget** | [**BoostPostRequestBudget**](BoostPostRequestBudget.md) |  |  |
|**currency** | **String** |  |  [optional] |
|**schedule** | [**BoostPostRequestSchedule**](BoostPostRequestSchedule.md) |  |  [optional] |
|**targeting** | [**BoostPostRequestTargeting**](BoostPostRequestTargeting.md) |  |  [optional] |
|**bidAmount** | **BigDecimal** | Max bid cap (Meta only) |  [optional] |
|**tracking** | [**BoostPostRequestTracking**](BoostPostRequestTracking.md) |  |  [optional] |
|**specialAdCategories** | [**List&lt;SpecialAdCategoriesEnum&gt;**](#List&lt;SpecialAdCategoriesEnum&gt;) | Meta only. Required for housing, employment, credit, or political ads. |  [optional] |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| ENGAGEMENT | &quot;engagement&quot; |
| TRAFFIC | &quot;traffic&quot; |
| AWARENESS | &quot;awareness&quot; |
| VIDEO_VIEWS | &quot;video_views&quot; |
| LEAD_GENERATION | &quot;lead_generation&quot; |
| CONVERSIONS | &quot;conversions&quot; |
| APP_PROMOTION | &quot;app_promotion&quot; |



## Enum: List&lt;SpecialAdCategoriesEnum&gt;

| Name | Value |
|---- | -----|
| HOUSING | &quot;HOUSING&quot; |
| EMPLOYMENT | &quot;EMPLOYMENT&quot; |
| CREDIT | &quot;CREDIT&quot; |
| ISSUES_ELECTIONS_POLITICS | &quot;ISSUES_ELECTIONS_POLITICS&quot; |



