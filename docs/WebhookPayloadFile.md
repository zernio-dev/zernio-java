

# WebhookPayloadFile

Webhook payload for file.created, file.updated and file.deleted. Carries the provider file id and the change only; read the file with `GET /v1/files/{id}`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Present on every event tied to a profile and absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once. Use it to route the event to your tenant without storing Zernio profile ids. |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadCalendarEventAccount**](WebhookPayloadCalendarEventAccount.md) |  |  |
|**_file** | [**WebhookPayloadCalendarEventCalendarEvent**](WebhookPayloadCalendarEventCalendarEvent.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| FILE_CREATED | &quot;file.created&quot; |
| FILE_UPDATED | &quot;file.updated&quot; |
| FILE_DELETED | &quot;file.deleted&quot; |



