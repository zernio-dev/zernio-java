

# UpdateBidStrategyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**adAccountId** | **String** | Platform ad account ID (Google customer ID, digits only). Defaults to the account&#39;s connected customer. |  [optional] |
|**customerId** | **String** | Alias of adAccountId, kept for existing callers |  [optional] |
|**name** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**targetCpa** | **BigDecimal** |  |  [optional] |
|**targetRoas** | **BigDecimal** |  |  [optional] |
|**targetImpressionShare** | [**GoogleTargetImpressionShare**](GoogleTargetImpressionShare.md) | Retargets a TARGET_IMPRESSION_SHARE strategy; location, percent and maxCpc are all written. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TARGET_CPA | &quot;TARGET_CPA&quot; |
| TARGET_ROAS | &quot;TARGET_ROAS&quot; |
| MAXIMIZE_CONVERSIONS | &quot;MAXIMIZE_CONVERSIONS&quot; |
| MAXIMIZE_CONVERSION_VALUE | &quot;MAXIMIZE_CONVERSION_VALUE&quot; |
| TARGET_IMPRESSION_SHARE | &quot;TARGET_IMPRESSION_SHARE&quot; |



