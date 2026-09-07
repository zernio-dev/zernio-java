

# UpdateAdCampaign200Response

Echoes back only the fields you sent, plus `updated`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**updated** | **Integer** | Local Ad documents mirrored. 0 on the empty-campaign path. |  [optional] |
|**budget** | [**AdBudget**](AdBudget.md) |  |  [optional] |
|**budgetLevel** | [**BudgetLevelEnum**](#BudgetLevelEnum) |  |  [optional] |
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** |  |  [optional] |
|**roasAverageFloor** | **BigDecimal** |  |  [optional] |
|**portfolioBidStrategyId** | **String** | Google only. Echoed back, but NOT mirrored onto local Ad documents (no column for it yet). |  [optional] |
|**platformSpecificData** | **Object** |  |  [optional] |



## Enum: BudgetLevelEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |



