

# AutomationStepOneOf3

Changes the daily budget by a percent: an increase needs `max`, the budget it stops at, and a decrease needs `min`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**by** | **String** | Up to +100% or down to -90%. |  |
|**max** | **BigDecimal** |  |  [optional] |
|**min** | **BigDecimal** |  |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| BUDGET | &quot;budget&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_CHANGE_BUDGET | &quot;ads.change_budget&quot; |



