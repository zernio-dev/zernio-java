

# AutomationOneOf2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Only a sequence can be a draft. |  |
|**trigger** | [**AutomationPostSchedule**](AutomationPostSchedule.md) |  |  |
|**subjects** | [**AutomationPostSubjects**](AutomationPostSubjects.md) |  |  |
|**filter** | [**AutomationFactCondition**](AutomationFactCondition.md) |  |  [optional] |
|**steps** | [**List&lt;ScheduledAutomationDefinitionStepsInner&gt;**](ScheduledAutomationDefinitionStepsInner.md) |  |  |
|**limits** | [**AutomationEventLimits**](AutomationEventLimits.md) |  |  [optional] |
|**id** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**version** | **String** | Send it back as &#x60;If-Match&#x60; when editing, so an edit made after someone else saved is refused. |  |
|**lastCheckAt** | **OffsetDateTime** | Null until an ad rule first checks. Always null for event and scheduled automations; their checks list when they ran. |  |
|**nextCheckAt** | **OffsetDateTime** | Null while paused. Always null for event, scheduled and sequence automations. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**template** | [**AutomationRecordTemplate**](AutomationRecordTemplate.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| SCHEDULED | &quot;scheduled&quot; |



