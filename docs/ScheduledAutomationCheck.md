

# ScheduledAutomationCheck

One check of a scheduled automation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**automationId** | **String** |  |  |
|**checkedAt** | **OffsetDateTime** |  |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) |  |  |
|**evaluated** | **Integer** | Posts judged. |  |
|**analyticsSyncedAt** | **OffsetDateTime** | The oldest analytics sync among the posts judged: their numbers are as of then. |  |
|**matched** | [**List&lt;ScheduledAutomationCheckMatchedInner&gt;**](ScheduledAutomationCheckMatchedInner.md) | Up to 20 matching posts. |  |
|**actions** | [**List&lt;ScheduledAutomationCheckActionsInner&gt;**](ScheduledAutomationCheckActionsInner.md) |  |  |
|**error** | **String** |  |  |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| NO_MATCH | &quot;no_match&quot; |
| COOLDOWN | &quot;cooldown&quot; |
| DAILY_LIMIT | &quot;daily_limit&quot; |
| FAILED | &quot;failed&quot; |



