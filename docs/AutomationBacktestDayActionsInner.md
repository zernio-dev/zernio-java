

# AutomationBacktestDayActionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**subject** | [**AutomationBacktestDayActionsInnerSubject**](AutomationBacktestDayActionsInnerSubject.md) |  |  |
|**group** | **String** | For an automation with groups, the group the campaign was judged in. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**budget** | [**AutomationBacktestDayActionsInnerBudget**](AutomationBacktestDayActionsInnerBudget.md) |  |  [optional] |
|**skipped** | [**SkippedEnum**](#SkippedEnum) | Why it would have been skipped. Absent when it would have acted. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_PAUSE | &quot;ads.pause&quot; |
| ADS_ACTIVATE | &quot;ads.activate&quot; |
| ADS_SET_BUDGET | &quot;ads.set_budget&quot; |
| ADS_DUPLICATE | &quot;ads.duplicate&quot; |
| ADS_EDIT_NAME | &quot;ads.edit_name&quot; |
| ADS_SET_BID | &quot;ads.set_bid&quot; |
| ADS_SET_TARGET | &quot;ads.set_target&quot; |
| ADS_REALLOCATE_BUDGET | &quot;ads.reallocate_budget&quot; |
| NOTIFY_SEND | &quot;notify.send&quot; |



## Enum: SkippedEnum

| Name | Value |
|---- | -----|
| BUDGET_UNKNOWN | &quot;budget_unknown&quot; |
| AT_LIMIT | &quot;at_limit&quot; |
| ALREADY_AT_AMOUNT | &quot;already_at_amount&quot; |



