

# EstimateAdReachRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Social account ID on the target ad platform. |  |
|**spec** | [**TargetingSpec**](TargetingSpec.md) | The targeting spec to estimate. Same shape used by POST /v1/ads/create. |  |
|**optimizationGoal** | **String** | Optional. The optimization goal the estimate should assume (platform&#39;s own vocabulary, e.g. Meta &#x60;REACH&#x60;, &#x60;LINK_CLICKS&#x60;, &#x60;OFFSITE_CONVERSIONS&#x60;). Some platforms vary the estimate by goal; omit to use the platform default.  |  [optional] |



