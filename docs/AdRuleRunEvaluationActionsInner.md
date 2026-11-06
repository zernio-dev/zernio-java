

# AdRuleRunEvaluationActionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**objectId** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**reason** | **String** | Why it was skipped or failed, for example &#x60;already_paused&#x60;. |  [optional] |
|**previousDailyBudget** | **BigDecimal** |  |  [optional] |
|**newDailyBudget** | **BigDecimal** |  |  [optional] |
|**previousName** | **String** |  |  [optional] |
|**newName** | **String** |  |  [optional] |
|**previousBidAmount** | **BigDecimal** |  |  [optional] |
|**newBidAmount** | **BigDecimal** |  |  [optional] |
|**targetMetric** | [**TargetMetricEnum**](#TargetMetricEnum) |  |  [optional] |
|**previousTarget** | **BigDecimal** |  |  [optional] |
|**newTarget** | **BigDecimal** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAUSE | &quot;pause&quot; |
| ACTIVATE | &quot;activate&quot; |
| ADJUST_BUDGET | &quot;adjust_budget&quot; |
| ADJUST_BID | &quot;adjust_bid&quot; |
| ADJUST_TARGET | &quot;adjust_target&quot; |
| REALLOCATE_BUDGET | &quot;reallocate_budget&quot; |
| DUPLICATE | &quot;duplicate&quot; |
| EDIT_NAME | &quot;edit_name&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DONE | &quot;done&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |



## Enum: TargetMetricEnum

| Name | Value |
|---- | -----|
| CPA | &quot;cpa&quot; |
| ROAS | &quot;roas&quot; |



