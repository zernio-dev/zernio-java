

# AdRuleAutomationCheck

One check of an ad rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**automationId** | **String** |  |  |
|**checkedAt** | **OffsetDateTime** |  |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) |  |  |
|**evaluated** | **Integer** | Objects judged. |  |
|**subjects** | [**List&lt;AdRuleAutomationCheckSubjectsInner&gt;**](AdRuleAutomationCheckSubjectsInner.md) |  |  |
|**actions** | [**List&lt;AdRuleAutomationCheckActionsInner&gt;**](AdRuleAutomationCheckActionsInner.md) |  |  |
|**notification** | [**AdRuleAutomationCheckNotification**](AdRuleAutomationCheckNotification.md) |  |  |
|**error** | **String** |  |  |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| COOLDOWN | &quot;cooldown&quot; |
| NO_MATCH | &quot;no_match&quot; |
| FAILED | &quot;failed&quot; |



