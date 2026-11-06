

# WebhookPayloadAdRuleTriggeredObjectsInnerActionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Action result.  - &#x60;skipped&#x60;: the action could not or need not apply (already paused or active, budget at its limit, a budget that is unknown, not daily or set at another level, no live ads, or a permanent refusal from the platform). - &#x60;failed&#x60;: it errored and will be retried on the next run. |  |
|**reason** | **String** | Why the action was skipped or failed, or the platform&#39;s message. Null when done.  Skipped: &#x60;already_paused&#x60;, &#x60;already_active&#x60;, &#x60;at_limit&#x60;, &#x60;budget_unknown&#x60;, &#x60;budget_not_daily&#x60;, &#x60;budget_level_mismatch&#x60;, &#x60;no_live_ads&#x60;, &#x60;budget_shared&#x60;, &#x60;portfolio_bid_strategy&#x60;, &#x60;unsupported_bid_strategy&#x60;, &#x60;no_target_cpa&#x60;, &#x60;no_target_roas&#x60;.  &#x60;daily_limit_reached&#x60;: held back by the action&#39;s &#x60;maxChangesPerDay&#x60;. &#x60;ads_allowance_exceeded&#x60;: a reactivation or budget increase for a team past its free live-ads allowance.  &#x60;reallocation_incomplete&#x60; (failed): a receiver left alone because a giver&#39;s cut did not apply, tried again next run. |  |
|**previousDailyBudget** | **BigDecimal** | On &#x60;adjust_budget&#x60;, the daily budget before the change, in the ad account currency. Null otherwise. |  |
|**newDailyBudget** | **BigDecimal** | On &#x60;adjust_budget&#x60;, the daily budget after the change. Null when nothing changed. |  |
|**previousName** | **String** | On &#x60;edit_name&#x60;, the object&#39;s name before the change. Null otherwise. |  |
|**newName** | **String** | On &#x60;edit_name&#x60;, the name after the change. Null when nothing changed. |  |
|**previousBidAmount** | **BigDecimal** | On &#x60;adjust_bid&#x60;, the cap before the change. Null otherwise. |  |
|**newBidAmount** | **BigDecimal** | On &#x60;adjust_bid&#x60;, the cap after the change. Null when nothing changed. |  |
|**targetMetric** | [**TargetMetricEnum**](#TargetMetricEnum) | On &#x60;adjust_target&#x60;, which target moved. Null otherwise. |  |
|**previousTarget** | **BigDecimal** | On &#x60;adjust_target&#x60;, the target before the change. Null otherwise. |  |
|**newTarget** | **BigDecimal** | On &#x60;adjust_target&#x60;, the target after the change. Null when nothing changed. |  |



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



