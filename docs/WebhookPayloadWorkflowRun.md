

# WebhookPayloadWorkflowRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Event id, the dedupe key. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
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



