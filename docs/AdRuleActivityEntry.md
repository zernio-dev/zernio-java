

# AdRuleActivityEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable ID of this entry. |  |
|**ranAt** | **OffsetDateTime** |  |  |
|**ruleId** | **String** |  |  |
|**ruleName** | **String** | The rule&#39;s name when it acted. |  |
|**platform** | **String** |  |  |
|**accountId** | **String** | The ads connection the rule runs on. |  |
|**adAccountId** | **String** |  |  |
|**level** | [**LevelEnum**](#LevelEnum) |  |  |
|**objectId** | **String** | Platform ID of the campaign or ad set. |  |
|**objectName** | **String** | Its name when the rule acted. |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**reason** | **String** | Why it was skipped or failed, for example &#x60;already_paused&#x60;. |  |
|**previousDailyBudget** | **BigDecimal** |  |  |
|**newDailyBudget** | **BigDecimal** |  |  |
|**currency** | **String** |  |  |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |



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



