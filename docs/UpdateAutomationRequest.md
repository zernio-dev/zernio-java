

# UpdateAutomationRequest

Any top-level field of the automation's kind (see `AutomationDefinition`); the fields of another kind are refused.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**description** | **String** | Sequences and flows. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;draft&#x60; only for a sequence or a flow that has not left draft. |  [optional] |
|**trigger** | **Object** | The trigger of the automation&#39;s kind. |  [optional] |
|**orTriggers** | **List&lt;Object&gt;** | Comment to DM. |  [optional] |
|**graph** | **Object** | Comment to DM and flows: the whole graph, as read. |  [optional] |
|**subjects** | [**UpdateAutomationRequestSubjects**](UpdateAutomationRequestSubjects.md) |  |  [optional] |
|**filter** | [**AutomationFactCondition**](AutomationFactCondition.md) |  |  [optional] |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  [optional] |
|**alert** | [**AutomationAlert**](AutomationAlert.md) |  |  [optional] |
|**steps** | [**List&lt;UpdateAutomationRequestStepsInner&gt;**](UpdateAutomationRequestStepsInner.md) | The steps the automation&#39;s kind takes. |  [optional] |
|**limits** | **Object** | The limits of the automation&#39;s kind. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



