

# UpdateAutomationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**trigger** | [**AutomationTrigger**](AutomationTrigger.md) |  |  [optional] |
|**subjects** | [**UpdateAutomationRequestSubjects**](UpdateAutomationRequestSubjects.md) |  |  [optional] |
|**filter** | [**AutomationFactCondition**](AutomationFactCondition.md) |  |  [optional] |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  [optional] |
|**alert** | [**AutomationAlert**](AutomationAlert.md) |  |  [optional] |
|**steps** | [**List&lt;UpdateAutomationRequestStepsInner&gt;**](UpdateAutomationRequestStepsInner.md) | The steps the automation&#39;s kind takes. |  [optional] |
|**limits** | [**UpdateAutomationRequestLimits**](UpdateAutomationRequestLimits.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



