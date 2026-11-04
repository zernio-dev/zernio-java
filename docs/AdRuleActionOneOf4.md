

# AdRuleActionOneOf4

Either `amount`, or `direction`, `percent` and `limit`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Move the bid cap or cost cap of a Meta ad set, in the ad account currency. Ad set rules on Meta only. An ad set without a cap is skipped with &#x60;no_bid_cap&#x60;. |  |
|**amount** | **BigDecimal** | The cap to set. |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**percent** | **Integer** | Step size. A decrease is at most 90. |  [optional] |
|**limit** | **BigDecimal** | The cap never goes above this on an increase, or below it on a decrease. |  [optional] |
|**maxChangesPerDay** | **Integer** | At most this many objects changed in any 24 hours, across runs. Matches over the limit are skipped with &#x60;daily_limit_reached&#x60; and tried again later. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADJUST_BID | &quot;adjust_bid&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INCREASE | &quot;increase&quot; |
| DECREASE | &quot;decrease&quot; |



