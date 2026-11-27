

# GraphAutomationDefinition

Any automation sent as an automation graph. It is saved as its own shape would be.  - A comment to DM keeps its fixed node ids (`dm`, `reply`, `like`, `hide`, `delay`, ...) and may carry its DM door as a second trigger with its own `entry`. - A flow's trigger settings go on its trigger node, added when the graph has none. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** | Sequences and flows. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**graph** | [**AutomationGraph**](AutomationGraph.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



