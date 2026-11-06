

# EventAutomationDefinition

Runs when something happens in Zernio, such as a post failing, and notifies. Unknown fields are refused.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | A new event automation is on unless &#x60;paused&#x60;. |  [optional] |
|**trigger** | [**AutomationEventTrigger**](AutomationEventTrigger.md) |  |  |
|**steps** | [**List&lt;AutomationNotifyStep&gt;**](AutomationNotifyStep.md) |  |  |
|**limits** | [**AutomationEventLimits**](AutomationEventLimits.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



