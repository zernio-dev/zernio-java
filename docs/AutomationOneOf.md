

# AutomationOneOf


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**trigger** | [**AutomationScheduleTrigger**](AutomationScheduleTrigger.md) |  |  |
|**subjects** | [**AutomationSubjects**](AutomationSubjects.md) |  |  |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  |
|**alert** | [**AutomationAlert**](AutomationAlert.md) |  |  [optional] |
|**steps** | [**List&lt;AutomationStep&gt;**](AutomationStep.md) |  |  |
|**limits** | [**AutomationLimits**](AutomationLimits.md) |  |  [optional] |
|**id** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**version** | **String** | Send it back as &#x60;If-Match&#x60; when editing, so an edit made after someone else saved is refused. |  |
|**lastCheckAt** | **OffsetDateTime** | Null until an ad rule first checks. Always null for event and scheduled automations; their checks list when they ran. |  |
|**nextCheckAt** | **OffsetDateTime** | Null while paused. Always null for event and scheduled automations. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**template** | [**AutomationRecordTemplate**](AutomationRecordTemplate.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| AD_RULE | &quot;ad_rule&quot; |



