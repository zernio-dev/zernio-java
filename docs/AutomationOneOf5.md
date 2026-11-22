

# AutomationOneOf5


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Only a sequence or a flow can be a draft. |  |
|**trigger** | [**FlowAutomationDefinitionTrigger**](FlowAutomationDefinitionTrigger.md) |  |  |
|**graph** | [**FlowAutomationDefinitionGraph**](FlowAutomationDefinitionGraph.md) |  |  |
|**id** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**version** | **String** | Send it back as &#x60;If-Match&#x60; when editing, so an edit made after someone else saved is refused. |  |
|**lastCheckAt** | **OffsetDateTime** | Null until an ad rule first checks. Always null for every other kind; the checks of event and scheduled automations list when they ran. |  |
|**nextCheckAt** | **OffsetDateTime** | Null while paused. Always null for every kind but ad rules. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**template** | [**AutomationRecordTemplate**](AutomationRecordTemplate.md) |  |  [optional] |
|**platform** | **String** | The account&#39;s platform. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| WORKFLOW | &quot;workflow&quot; |



