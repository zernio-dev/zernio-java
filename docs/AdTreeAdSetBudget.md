

# AdTreeAdSetBudget

Effective budget at this level (back-compat). For CBO campaigns this mirrors the parent campaign's budget; for ABO this is the ad-set-specific budget. Use `adSetBudget` / parent `campaignBudget` + `budgetLevel` to disambiguate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



