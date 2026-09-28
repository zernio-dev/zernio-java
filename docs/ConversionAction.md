

# ConversionAction

A Google Ads conversion action, e.g. a WEBPAGE conversion created via `createConversionAction`. Returned by `listConversionActions` and `createConversionAction`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Google Ads conversion action id. |  |
|**name** | **String** |  |  |
|**type** | **String** | Google&#39;s ConversionActionType, e.g. WEBPAGE, UPLOAD_CLICKS. |  |
|**status** | **String** | Google&#39;s ConversionActionStatus, e.g. ENABLED, REMOVED, HIDDEN. |  |
|**category** | **String** | Google&#39;s ConversionActionCategory, e.g. DEFAULT, PURCHASE, LEAD. |  |
|**origin** | **String** | Google&#39;s ConversionOrigin, e.g. WEBSITE, APP. Together with category it names the goal the action belongs to (see GET /v1/ads/conversions/goals). |  [optional] |
|**primaryForGoal** | **Boolean** | true &#x3D; primary (counts toward bidding when its goal is biddable), false &#x3D; secondary. Change it with PATCH /v1/ads/conversions/actions/{actionId}. |  [optional] |
|**defaultValue** | **BigDecimal** | Value recorded when the conversion carries none. |  [optional] |
|**defaultCurrency** | **String** | ISO 4217 currency of defaultValue. |  [optional] |
|**alwaysUseDefaultValue** | **Boolean** | true &#x3D; defaultValue is used even when the conversion sends its own value. |  [optional] |
|**countingType** | **String** | Google&#39;s ConversionActionCountingType: ONE_PER_CLICK or MANY_PER_CLICK. |  [optional] |
|**clickThroughLookbackWindowDays** | **Integer** | Days after an ad click a conversion is still credited (1 to 90). |  [optional] |
|**viewThroughLookbackWindowDays** | **Integer** | Days after an ad view a conversion is still credited (1 to 30). |  [optional] |
|**tagSnippets** | [**List&lt;ConversionActionTagSnippetsInner&gt;**](ConversionActionTagSnippetsInner.md) | The code a customer pastes onto their site. Present for types Google generates a snippet for (e.g. WEBPAGE); empty otherwise.  |  |



