

# ListAdAudiences200ResponseAudiencesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The Zernio audience id. Pass this as audienceId on GET /v1/ads/audiences/{audienceId} and the companies/users upload endpoints. Null when the audience was not created through Zernio. |  [optional] |
|**accountId** | **String** | Account the audience was created against. Returned for saved_targeting items. |  [optional] |
|**platformAudienceId** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;reddit_engagement&#x60;, &#x60;third_party&#x60; and &#x60;in_market&#x60; are listed from Reddit (engagement retargeting, and Reddit&#39;s own audiences) so they can be targeted. Zernio cannot create them. |  [optional] |
|**spec** | [**TargetingSpec**](TargetingSpec.md) |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**size** | **Integer** |  |  [optional] |
|**status** | **String** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_LIST | &quot;customer_list&quot; |
| COMPANY_LIST | &quot;company_list&quot; |
| ENGAGEMENT | &quot;engagement&quot; |
| META_ENGAGEMENT | &quot;meta_engagement&quot; |
| TIKTOK_ENGAGEMENT | &quot;tiktok_engagement&quot; |
| PINTEREST_ENGAGEMENT | &quot;pinterest_engagement&quot; |
| WEBSITE | &quot;website&quot; |
| WEBSITE_RETARGETING | &quot;website_retargeting&quot; |
| LOOKALIKE | &quot;lookalike&quot; |
| SAVED_TARGETING | &quot;saved_targeting&quot; |
| REDDIT_ENGAGEMENT | &quot;reddit_engagement&quot; |
| THIRD_PARTY | &quot;third_party&quot; |
| IN_MARKET | &quot;in_market&quot; |



