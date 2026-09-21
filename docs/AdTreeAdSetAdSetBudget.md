

# AdTreeAdSetAdSetBudget

Ad-set-level budget (ABO). Null for CBO campaigns where the budget is set on the campaign.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**daily** | **BigDecimal** | LinkedIn only. See &#x60;budget.daily&#x60;. |  [optional] |
|**lifetime** | **BigDecimal** | LinkedIn only. See &#x60;budget.lifetime&#x60;. |  [optional] |
|**pacing** | **String** | LinkedIn only. See &#x60;budget.pacing&#x60;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



