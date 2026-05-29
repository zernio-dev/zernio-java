

# CreateWorkflowRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**accountId** | **String** |  |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**nodes** | [**List&lt;WorkflowNode&gt;**](WorkflowNode.md) |  |  [optional] |
|**edges** | [**List&lt;WorkflowEdge&gt;**](WorkflowEdge.md) |  |  [optional] |
|**entryNodeId** | **String** | The trigger node id; derived from the single trigger node if omitted |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| WHATSAPP | &quot;whatsapp&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TELEGRAM | &quot;telegram&quot; |
| TWITTER | &quot;twitter&quot; |
| BLUESKY | &quot;bluesky&quot; |
| REDDIT | &quot;reddit&quot; |



