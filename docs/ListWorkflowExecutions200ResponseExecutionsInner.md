

# ListWorkflowExecutions200ResponseExecutionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**currentNodeId** | **String** |  |  [optional] |
|**waitingFor** | [**ListWorkflowExecutions200ResponseExecutionsInnerWaitingFor**](ListWorkflowExecutions200ResponseExecutionsInnerWaitingFor.md) |  |  [optional] |
|**variables** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**platformIdentifier** | **String** |  |  [optional] |
|**conversationId** | **String** |  |  [optional] |
|**stepCount** | **Integer** |  |  [optional] |
|**lastError** | **String** |  |  [optional] |
|**resumeAt** | **OffsetDateTime** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**completedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| WAITING | &quot;waiting&quot; |
| COMPLETED | &quot;completed&quot; |
| EXITED | &quot;exited&quot; |
| FAILED | &quot;failed&quot; |



