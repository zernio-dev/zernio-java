

# AutomationRecord


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Only a sequence or a flow can be a draft. |  |
|**version** | **String** | Send it back as &#x60;If-Match&#x60; when editing, so an edit made after someone else saved is refused. |  |
|**lastCheckAt** | **OffsetDateTime** | Null until an ad rule first checks. Always null for every other kind; the checks of event and scheduled automations list when they ran. |  |
|**nextCheckAt** | **OffsetDateTime** | Null while paused. Always null for every kind but ad rules. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**template** | [**AutomationRecordTemplate**](AutomationRecordTemplate.md) |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| AD_RULE | &quot;ad_rule&quot; |
| EVENT | &quot;event&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| SEQUENCE | &quot;sequence&quot; |
| COMMENT | &quot;comment&quot; |
| WORKFLOW | &quot;workflow&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



