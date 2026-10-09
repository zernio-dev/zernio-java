

# WebhookPayloadWorkflowRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Event id, the dedupe key. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**workflow** | [**WebhookPayloadWorkflowRunWorkflow**](WebhookPayloadWorkflowRunWorkflow.md) |  |  |
|**execution** | [**WebhookPayloadWorkflowRunExecution**](WebhookPayloadWorkflowRunExecution.md) |  |  |
|**conversation** | [**WebhookPayloadWorkflowRunConversation**](WebhookPayloadWorkflowRunConversation.md) |  |  |
|**contact** | [**WebhookPayloadContactTagContact**](WebhookPayloadContactTagContact.md) |  |  |
|**trigger** | [**WebhookPayloadWorkflowRunTrigger**](WebhookPayloadWorkflowRunTrigger.md) |  |  |
|**error** | **String** | workflow.run.failed only: which node failed and why. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WORKFLOW_RUN_STARTED | &quot;workflow.run.started&quot; |
| WORKFLOW_RUN_COMPLETED | &quot;workflow.run.completed&quot; |
| WORKFLOW_RUN_FAILED | &quot;workflow.run.failed&quot; |



