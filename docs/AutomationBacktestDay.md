

# AutomationBacktestDay


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **LocalDate** |  |  |
|**checks** | **Integer** | Checks the schedule would have run that day. 0 on a day it skips. |  |
|**evaluated** | **Integer** | The most objects any of the day&#39;s checks judged. |  |
|**matched** | **Integer** | The most objects any of the day&#39;s checks matched. |  |
|**heldBack** | **Integer** | Matches left alone all day by the cooldown or a cap. |  |
|**actions** | [**List&lt;AutomationBacktestDayActionsInner&gt;**](AutomationBacktestDayActionsInner.md) |  |  |



