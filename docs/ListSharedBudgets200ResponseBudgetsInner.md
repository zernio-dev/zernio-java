

# ListSharedBudgets200ResponseBudgetsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Numeric budget id; pass as sharedBudgetId. |  [optional] |
|**name** | **String** |  |  [optional] |
|**amount** | **BigDecimal** | In the account&#39;s currency units. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**deliveryMethod** | **String** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**campaignCount** | **Integer** | campaign_budget.reference_count |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



