

# AdRuleActionOneOf3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Change the daily budget. Not on ad-level rules (an ad has no budget), and on Google it needs a campaign-level rule (ad groups have no budget of their own). |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**percent** | **Integer** | Change in percent: up to 100 for an increase, up to 90 for a decrease. |  |
|**limit** | **BigDecimal** | The budget never goes above this on an increase, or below it on a decrease, in the ad account currency. |  |
|**maxChangesPerDay** | **Integer** | At most this many objects changed in any 24 hours, across runs. Matches over the limit are skipped with &#x60;daily_limit_reached&#x60; and tried again later. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADJUST_BUDGET | &quot;adjust_budget&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INCREASE | &quot;increase&quot; |
| DECREASE | &quot;decrease&quot; |



