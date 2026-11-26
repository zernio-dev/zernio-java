

# GraphAutomationDefinition

An ad rule, event or scheduled automation or sequence sent as an automation graph. It is saved as its own shape would be.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** | Sequences. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**graph** | [**AutomationGraph**](AutomationGraph.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



