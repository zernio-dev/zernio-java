

# UpdateBidStrategyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**customerId** | **String** | Numeric Google Ads customer id (no dashes). Defaults to the account&#39;s connected customer. |  [optional] |
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



