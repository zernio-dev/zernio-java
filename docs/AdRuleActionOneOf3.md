

# AdRuleActionOneOf3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Change the daily budget. Google ad groups have no budget of their own, so on Google it needs a campaign-level rule. |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**percent** | **Integer** | Change in percent: up to 100 for an increase, up to 90 for a decrease. |  |
|**limit** | **BigDecimal** | The budget never goes above this on an increase, or below it on a decrease, in the ad account currency. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADJUST_BUDGET | &quot;adjust_budget&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INCREASE | &quot;increase&quot; |
| DECREASE | &quot;decrease&quot; |



