

# CreateBidStrategyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**adAccountId** | **String** | Platform ad account ID (Google customer ID, digits only). Defaults to the account&#39;s connected customer. |  [optional] |
|**customerId** | **String** | Alias of adAccountId, kept for existing callers |  [optional] |
|**name** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**targetCpa** | **BigDecimal** | Required when type is TARGET_CPA, in the account&#39;s currency units. |  [optional] |
|**targetRoas** | **BigDecimal** | Required when type is TARGET_ROAS; a multiplier (2.0 &#x3D; 2.0x). |  [optional] |
|**targetImpressionShare** | [**GoogleTargetImpressionShare**](GoogleTargetImpressionShare.md) | Required when type is TARGET_IMPRESSION_SHARE, and refused with any other type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TARGET_CPA | &quot;TARGET_CPA&quot; |
| TARGET_ROAS | &quot;TARGET_ROAS&quot; |
| MAXIMIZE_CONVERSIONS | &quot;MAXIMIZE_CONVERSIONS&quot; |
| MAXIMIZE_CONVERSION_VALUE | &quot;MAXIMIZE_CONVERSION_VALUE&quot; |
| TARGET_IMPRESSION_SHARE | &quot;TARGET_IMPRESSION_SHARE&quot; |



