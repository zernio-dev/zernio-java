

# CommentAutomationDefinition

Comment to DM: a comment matching keywords (or a live comment, a story reply or a story mention on Instagram) runs a graph of steps with fixed ids. The same automation `/v1/comment-automations` serves.  Only the graphs that automation can hold are stored: read one to see the shapes it takes, and edit from there. Any other graph is refused at `graph`, naming the nodes and edges it would not keep. Unknown fields are refused. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**trigger** | [**CommentAutomationDefinitionTrigger**](CommentAutomationDefinitionTrigger.md) |  |  |
|**orTriggers** | [**List&lt;CommentAutomationDefinitionOrTriggersInner&gt;**](CommentAutomationDefinitionOrTriggersInner.md) | A DM with the same keywords also starts it (&#x60;dm.keyword&#x60;), at the decision and with no comment to act on. Comment triggers with keywords only. |  [optional] |
|**graph** | [**CommentAutomationDefinitionGraph**](CommentAutomationDefinitionGraph.md) |  |  |
|**limits** | [**CommentAutomationDefinitionLimits**](CommentAutomationDefinitionLimits.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



