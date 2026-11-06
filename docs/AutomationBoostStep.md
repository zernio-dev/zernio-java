

# AutomationBoostStep

Promotes each matched Facebook or Instagram post once, as a Meta ad with a lifetime budget. Posts on other platforms are not boosted. It needs the Ads add-on.  One boost step per automation, and `limits.maxChangesPerDay` (up to 20) is required: the most posts boosted in a day. At most 5 posts are boosted per check. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**adAccountId** | **String** | The Meta ad account that pays, from &#x60;GET /v1/ads/accounts&#x60;. |  |
|**budget** | **BigDecimal** | The whole spend of one boost, in the ad account currency. |  |
|**days** | **Integer** | How long each boost runs. |  |
|**goal** | [**GoalEnum**](#GoalEnum) |  |  [optional] |
|**countries** | **List&lt;String&gt;** | ISO 3166 alpha-2 codes. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_BOOST_POST | &quot;ads.boost_post&quot; |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| ENGAGEMENT | &quot;engagement&quot; |
| AWARENESS | &quot;awareness&quot; |
| VIDEO_VIEWS | &quot;video_views&quot; |



