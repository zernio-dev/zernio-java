

# ScheduledAutomationDefinition

Checks a profile's recent posts on a schedule. Each post that matches `filter` is notified about, and can be boosted. At most 20 posts are acted on per check. Unknown fields are refused. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | A new scheduled automation is on unless &#x60;paused&#x60;. |  [optional] |
|**trigger** | [**AutomationPostSchedule**](AutomationPostSchedule.md) |  |  |
|**subjects** | [**AutomationPostSubjects**](AutomationPostSubjects.md) |  |  |
|**filter** | [**AutomationFactCondition**](AutomationFactCondition.md) |  |  [optional] |
|**steps** | [**List&lt;ScheduledAutomationDefinitionStepsInner&gt;**](ScheduledAutomationDefinitionStepsInner.md) |  |  |
|**limits** | [**AutomationEventLimits**](AutomationEventLimits.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



