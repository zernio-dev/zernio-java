

# AutomationBacktestTotals


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | **Integer** | Actions it would have taken. Skipped ones are not counted. |  |
|**pauses** | **Integer** |  |  |
|**activations** | **Integer** |  |  |
|**budgetRaised** | **Integer** | Budget changes that raised a budget. |  |
|**budgetLowered** | **Integer** | Budget changes that lowered a budget. |  |
|**budgetChange** | **BigDecimal** | The net budget change across every budget action, in &#x60;currency&#x60;. |  |
|**notifications** | **Integer** |  |  |
|**skipped** | **Integer** | Actions planned but skipped. |  |
|**subjects** | **Integer** | Distinct objects it would have acted on. |  |
|**heldBack** | **Integer** | Matches left alone by the cooldown or a cap, summed over the days. |  |
|**daysWithActions** | **Integer** |  |  |



