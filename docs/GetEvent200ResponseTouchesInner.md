

# GetEvent200ResponseTouchesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**at** | **OffsetDateTime** |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) |  |  [optional] |
|**platform** | **String** | The ad platform of the campaign, the one an ad click&#39;s click id names (gclid reads as googleads), or the one a survey answer names (Instagram reads as facebook). |  [optional] |
|**adAccountId** | **String** |  |  [optional] |
|**campaignId** | **String** | The campaign the touch resolved to; null for a touch that named none (search, referral). |  [optional] |
|**campaignName** | **String** | The campaign&#39;s name in the ad account, when Zernio holds it. |  [optional] |
|**detail** | [**GetEvent200ResponseTouchesInnerDetail**](GetEvent200ResponseTouchesInnerDetail.md) |  |  [optional] |
|**credit** | **Map&lt;String, BigDecimal&gt;** | The share of the event (0 to 1) this touch gets per model: first_touch, last_non_direct, linear, position_based, time_decay, w_shaped. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| AD_CLICK | &quot;ad_click&quot; |
| PAID | &quot;paid&quot; |
| EMAIL | &quot;email&quot; |
| SOCIAL | &quot;social&quot; |
| CAMPAIGN | &quot;campaign&quot; |
| ORGANIC_SEARCH | &quot;organic_search&quot; |
| AI_ASSISTANT | &quot;ai_assistant&quot; |
| REFERRAL | &quot;referral&quot; |
| LEAD_FORM | &quot;lead_form&quot; |
| EVENT | &quot;event&quot; |
| SURVEY | &quot;survey&quot; |



