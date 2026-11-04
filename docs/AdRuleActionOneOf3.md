

# AdRuleActionOneOf3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Set the daily budget to an exact amount, such as a reset every midnight. Same level rules as the percent change. |  |
|**amount** | **BigDecimal** | The daily budget to set, in the ad account currency. An object already at it is skipped with &#x60;already_at_amount&#x60;. |  |
|**maxChangesPerDay** | **Integer** | At most this many objects changed in any 24 hours, across runs. Matches over the limit are skipped with &#x60;daily_limit_reached&#x60; and tried again later. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADJUST_BUDGET | &quot;adjust_budget&quot; |



