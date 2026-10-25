

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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAUSE | &quot;pause&quot; |
| ACTIVATE | &quot;activate&quot; |
| ADJUST_BUDGET | &quot;adjust_budget&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DONE | &quot;done&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |



