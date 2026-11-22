

# SequenceAutomationDefinition

Messages a contact over time from one account, starting when the contact is enrolled (`POST /v1/sequences/{sequenceId}/enroll`, a flow, or by hand). The same sequence `/v1/sequences` serves. Unknown fields are refused.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A new sequence is on unless &#x60;draft&#x60;. A draft can be activated; a sequence that ran can only be paused and activated again. |  [optional] |
|**trigger** | [**SequenceAutomationDefinitionTrigger**](SequenceAutomationDefinitionTrigger.md) |  |  |
|**steps** | [**List&lt;AutomationSequenceStep&gt;**](AutomationSequenceStep.md) | At least one step for an active sequence. Steps change only while it is a draft or paused. |  |
|**limits** | [**SequenceAutomationDefinitionLimits**](SequenceAutomationDefinitionLimits.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



