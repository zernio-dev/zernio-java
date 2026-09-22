

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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TARGET_CPA | &quot;TARGET_CPA&quot; |
| TARGET_ROAS | &quot;TARGET_ROAS&quot; |
| MAXIMIZE_CONVERSIONS | &quot;MAXIMIZE_CONVERSIONS&quot; |
| MAXIMIZE_CONVERSION_VALUE | &quot;MAXIMIZE_CONVERSION_VALUE&quot; |



