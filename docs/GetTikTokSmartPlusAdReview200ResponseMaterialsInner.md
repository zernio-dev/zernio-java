

# GetTikTokSmartPlusAdReview200ResponseMaterialsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adMaterialId** | **String** | TikTok &#x60;ad_material_id&#x60; of the creative inside this ad. |  [optional] |
|**materialType** | [**MaterialTypeEnum**](#MaterialTypeEnum) | Null for a creative TikTok added on its own or a carousel image. |  [optional] |
|**tiktokItemId** | **String** | The TikTok post id when the creative is a Spark post. |  [optional] |
|**videoId** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**operationStatus** | **String** | TikTok &#x60;material_operation_status&#x60;: ENABLE or DISABLE. |  [optional] |
|**reviewStatus** | **TikTokSmartPlusReviewStatus** |  |  [optional] |
|**rawReviewStatus** | **String** | TikTok &#x60;review_status&#x60;, verbatim. |  [optional] |
|**rejectReasons** | **List&lt;String&gt;** | Every distinct reason across &#x60;rejections&#x60;. Empty when approved. |  [optional] |
|**passedLocations** | **List&lt;String&gt;** |  |  [optional] |
|**rejections** | [**List&lt;TikTokReviewRejection&gt;**](TikTokReviewRejection.md) |  |  [optional] |



## Enum: MaterialTypeEnum

| Name | Value |
|---- | -----|
| SPARK_POST | &quot;spark_post&quot; |
| VIDEO | &quot;video&quot; |
| CAROUSEL | &quot;carousel&quot; |
| CATALOG_CAROUSEL | &quot;catalog_carousel&quot; |



