

# AutomationOneOf4


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Only a sequence or a flow can be a draft. |  |
|**trigger** | [**CommentAutomationDefinitionTrigger**](CommentAutomationDefinitionTrigger.md) |  |  |
|**orTriggers** | [**List&lt;CommentAutomationDefinitionOrTriggersInner&gt;**](CommentAutomationDefinitionOrTriggersInner.md) | A DM with the same keywords also starts it (&#x60;dm.keyword&#x60;), at the decision and with no comment to act on. Comment triggers with keywords only. |  [optional] |
|**graph** | [**CommentAutomationDefinitionGraph**](CommentAutomationDefinitionGraph.md) |  |  |
|**limits** | [**CommentAutomationDefinitionLimits**](CommentAutomationDefinitionLimits.md) |  |  |
|**id** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**version** | **String** | Send it back as &#x60;If-Match&#x60; when editing, so an edit made after someone else saved is refused. |  |
|**lastCheckAt** | **OffsetDateTime** | Null until an ad rule first checks. Always null for every other kind; the checks of event and scheduled automations list when they ran. |  |
|**nextCheckAt** | **OffsetDateTime** | Null while paused. Always null for every kind but ad rules. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**template** | [**AutomationRecordTemplate**](AutomationRecordTemplate.md) |  |  [optional] |
|**platform** | **String** | The account&#39;s platform. On TikTok, Threads, LinkedIn and YouTube it only posts the public reply. |  |
|**readOnly** | **Boolean** | Always true when present. Present when the graph only comes near what the automation does. It is read here and edited through &#x60;/v1/comment-automations&#x60;; an edit here is refused. |  [optional] |
|**stats** | **AutomationOneOf4AllOfStats** |  |  |



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



