

# WebhookPayloadAdRuleTriggeredObjectsInnerActionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;skipped&#x60; when the action could not or need not apply (already paused or active, budget at its limit, a budget that is unknown, not daily or set at another level, no live ads, or a permanent refusal from the platform), &#x60;failed&#x60; when it errored and will be retried on the next run. |  |
|**reason** | **String** | Why the action was skipped or failed: &#x60;already_paused&#x60;, &#x60;already_active&#x60;, &#x60;at_limit&#x60;, &#x60;budget_unknown&#x60;, &#x60;budget_not_daily&#x60;, &#x60;budget_level_mismatch&#x60;, &#x60;no_live_ads&#x60;, &#x60;ads_allowance_exceeded&#x60; (a reactivation or budget increase for a team past its free live-ads allowance), or the platform&#39;s message. Null when done. |  |
|**previousDailyBudget** | **BigDecimal** | On &#x60;adjust_budget&#x60;, the daily budget before the change, in the ad account currency. Null otherwise. |  |
|**newDailyBudget** | **BigDecimal** | On &#x60;adjust_budget&#x60;, the daily budget after the change. Null when nothing changed. |  |



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



