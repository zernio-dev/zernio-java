

# GetWorkflow200ResponseWorkflow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**entryNodeId** | **String** |  |  [optional] |
|**nodes** | [**List&lt;WorkflowNode&gt;**](WorkflowNode.md) |  |  [optional] |
|**edges** | [**List&lt;WorkflowEdge&gt;**](WorkflowEdge.md) |  |  [optional] |
|**totalStarted** | **Integer** |  |  [optional] |
|**totalCompleted** | **Integer** |  |  [optional] |
|**totalExited** | **Integer** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



