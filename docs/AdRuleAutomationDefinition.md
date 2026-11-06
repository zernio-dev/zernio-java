

# AdRuleAutomationDefinition

An ad rule. It is also readable under `/v1/ads/rules` with the same id. Unknown fields are refused.  To have a person OK each change before it is made, put an `approval.request` step before the `ads.*` step. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | A new ad rule stays paused unless &#x60;active&#x60;. |  [optional] |
|**trigger** | [**AutomationScheduleTrigger**](AutomationScheduleTrigger.md) |  |  |
|**subjects** | [**AutomationSubjects**](AutomationSubjects.md) |  |  |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  |
|**alert** | [**AutomationAlert**](AutomationAlert.md) |  |  [optional] |
|**steps** | [**List&lt;AutomationStep&gt;**](AutomationStep.md) |  |  |
|**limits** | [**AutomationLimits**](AutomationLimits.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



