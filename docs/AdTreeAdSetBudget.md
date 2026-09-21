

# AdTreeAdSetBudget

Effective budget at this level (back-compat). For CBO campaigns this mirrors the parent campaign's budget; for ABO this is the ad-set-specific budget. Use `adSetBudget` / parent `campaignBudget` + `budgetLevel` to disambiguate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**daily** | **BigDecimal** | LinkedIn only. The campaign&#39;s &#x60;dailyBudget&#x60;. LinkedIn allows a daily AND a lifetime budget on the same campaign, which &#x60;amount&#x60;/&#x60;type&#x60; cannot express (daily wins there); read &#x60;daily&#x60; and &#x60;lifetime&#x60; to see both. |  [optional] |
|**lifetime** | **BigDecimal** | LinkedIn only. The campaign&#39;s &#x60;totalBudget&#x60;, readable even when a daily budget is also set. |  [optional] |
|**pacing** | **String** | LinkedIn only. The campaign&#39;s &#x60;pacingStrategy&#x60;: how fast LinkedIn may spend the budget. Typically LINEAR or ACCELERATED; the list is open. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



