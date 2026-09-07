

# PortfolioBidStrategy

A Google Ads portfolio bid strategy: a named bidding strategy shared across campaigns, with its R.130 report metrics over the queried date range.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Numeric bid strategy id; pass as portfolioBidStrategyId or in the {strategyId} path. |  [optional] |
|**name** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**status** | **String** | ENABLED or REMOVED. |  [optional] |
|**campaignCount** | **Integer** | Number of campaigns currently attached. |  [optional] |
|**clicks** | **Integer** |  |  [optional] |
|**cost** | **BigDecimal** | Cost in the account&#39;s currency units (converted from micros). |  [optional] |
|**costPerConversion** | **BigDecimal** | Cost per conversion in the account&#39;s currency units. |  [optional] |
|**impressions** | **Integer** |  |  [optional] |
|**averageCpc** | **BigDecimal** | Average CPC in the account&#39;s currency units. |  [optional] |
|**conversions** | **BigDecimal** |  |  [optional] |
|**targetCpa** | **BigDecimal** | Current target, in the account&#39;s currency units. Null for a ROAS-family type (TARGET_ROAS, MAXIMIZE_CONVERSION_VALUE), or a Maximize type with no target set. Pre-fills the edit form&#39;s target field. |  [optional] |
|**targetRoas** | **BigDecimal** | Current target as a decimal multiplier (2.0 &#x3D; 2.0x). Null for a CPA-family type (TARGET_CPA, MAXIMIZE_CONVERSIONS), or a Maximize type with no target set. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TARGET_CPA | &quot;TARGET_CPA&quot; |
| TARGET_ROAS | &quot;TARGET_ROAS&quot; |
| MAXIMIZE_CONVERSIONS | &quot;MAXIMIZE_CONVERSIONS&quot; |
| MAXIMIZE_CONVERSION_VALUE | &quot;MAXIMIZE_CONVERSION_VALUE&quot; |



