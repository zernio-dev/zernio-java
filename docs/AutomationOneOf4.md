

# AutomationOneOf4


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Only a sequence can be a draft. |  |
|**trigger** | [**CommentAutomationDefinitionTrigger**](CommentAutomationDefinitionTrigger.md) |  |  |
|**orTriggers** | [**List&lt;CommentAutomationDefinitionOrTriggersInner&gt;**](CommentAutomationDefinitionOrTriggersInner.md) | A DM with the same keywords also starts it (&#x60;dm.keyword&#x60;), at the decision and with no comment to act on. Comment triggers with keywords only. |  [optional] |
|**graph** | [**CommentAutomationDefinitionGraph**](CommentAutomationDefinitionGraph.md) |  |  |
|**limits** | [**CommentAutomationDefinitionLimits**](CommentAutomationDefinitionLimits.md) |  |  |
|**id** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**version** | **String** | Send it back as &#x60;If-Match&#x60; when editing, so an edit made after someone else saved is refused. |  |
|**lastCheckAt** | **OffsetDateTime** | Null until an ad rule first checks. Always null for event and scheduled automations; their checks list when they ran. |  |
|**nextCheckAt** | **OffsetDateTime** | Null while paused. Always null for event, scheduled and sequence automations. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**template** | [**AutomationRecordTemplate**](AutomationRecordTemplate.md) |  |  [optional] |
|**platform** | **String** | The account&#39;s platform. On TikTok, Threads, LinkedIn and YouTube it only posts the public reply. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| COMMENT | &quot;comment&quot; |



