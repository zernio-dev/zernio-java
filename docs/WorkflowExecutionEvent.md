

# WorkflowExecutionEvent

One entry in a workflow execution's timeline. Emitted by the executor on every node visit and lifecycle transition, surfaced by `GET /v1/workflows/{workflowId}/executions/ {executionId}/events` for run inspection in the Runs UI. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**nodeId** | **String** | Present on &#x60;node_*&#x60; events |  [optional] |
|**nodeType** | **String** | Present on &#x60;node_*&#x60; events |  [optional] |
|**sourceHandle** | **String** | The edge handle the executor followed out of this node (see &#x60;WorkflowEdge.sourceHandle&#x60;) |  [optional] |
|**durationMs** | **Integer** | Node run time; present on &#x60;node_completed&#x60; and &#x60;node_failed&#x60; |  [optional] |
|**errorMessage** | **String** | Failure detail; present on &#x60;node_failed&#x60; and &#x60;execution_exited&#x60; |  [optional] |
|**meta** | **Map&lt;String, Object&gt;** | Per-node-type payload. Shape varies — see WorkflowNode &#x60;type&#x60;. Examples:   &#x60;send_message&#x60; → &#x60;{ messageType, text, recipient }&#x60;,   &#x60;webhook&#x60; → &#x60;{ url, method, statusCode, responseTimeMs, responsePreview }&#x60;,   &#x60;ai&#x60; → &#x60;{ model, provider, inputTokens, outputTokens, responsePreview }&#x60;,   &#x60;condition&#x60; → &#x60;{ matchedHandle, rulesEvaluated }&#x60;,   &#x60;a_b_split&#x60; → &#x60;{ percentage, chosen }&#x60;.  |  [optional] |
|**at** | **OffsetDateTime** | Event timestamp (UTC) |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| EXECUTION_STARTED | &quot;execution_started&quot; |
| EXECUTION_COMPLETED | &quot;execution_completed&quot; |
| EXECUTION_EXITED | &quot;execution_exited&quot; |
| EXECUTION_PAUSED | &quot;execution_paused&quot; |
| EXECUTION_RESUMED | &quot;execution_resumed&quot; |
| NODE_STARTED | &quot;node_started&quot; |
| NODE_COMPLETED | &quot;node_completed&quot; |
| NODE_FAILED | &quot;node_failed&quot; |
| NODE_SKIPPED | &quot;node_skipped&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILED | &quot;failed&quot; |
| PENDING | &quot;pending&quot; |



