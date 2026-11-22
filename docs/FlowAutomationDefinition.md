

# FlowAutomationDefinition

A flow: the workflow builder's graph of steps on one messaging account, the same flow `/v1/workflows` serves (versions and activation rules included). Its `kind` is `workflow`. Unknown fields are refused.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A new flow is &#x60;draft&#x60; (the default) or &#x60;active&#x60;, which needs a complete graph. An active or paused flow never goes back to draft, and only an active flow can be paused. |  [optional] |
|**trigger** | [**FlowAutomationDefinitionTrigger**](FlowAutomationDefinitionTrigger.md) |  |  |
|**graph** | [**FlowAutomationDefinitionGraph**](FlowAutomationDefinitionGraph.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



