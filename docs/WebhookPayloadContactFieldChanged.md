

# WebhookPayloadContactFieldChanged


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Event id, the dedupe key. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
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



