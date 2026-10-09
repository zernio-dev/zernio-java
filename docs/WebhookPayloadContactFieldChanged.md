

# WebhookPayloadContactFieldChanged


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Event id, the dedupe key. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**contact** | [**WebhookPayloadContactTagContact**](WebhookPayloadContactTagContact.md) |  |  |
|**field** | **String** | Custom field slug. |  |
|**previousValue** | **Object** |  |  |
|**value** | **Object** |  |  |
|**source** | [**SourceEnum**](#SourceEnum) | Who wrote the field: the API or dashboard, a workflow set_field node, or an automation. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CONTACT_FIELD_CHANGED | &quot;contact.field_changed&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| WORKFLOW | &quot;workflow&quot; |
| AUTOMATION | &quot;automation&quot; |



