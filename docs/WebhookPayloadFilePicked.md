

# WebhookPayloadFilePicked

Webhook payload for file.picked: the user picked files on a hosted picker page (`POST /v1/files/picker-sessions`), so the app may now open them. Every id was checked against Drive before the event fired.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Present on every event tied to a profile and absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once. Use it to route the event to your tenant without storing Zernio profile ids. |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadCalendarEventAccount**](WebhookPayloadCalendarEventAccount.md) |  |  |
|**picker** | [**WebhookPayloadFilePickedPicker**](WebhookPayloadFilePickedPicker.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| FILE_PICKED | &quot;file.picked&quot; |



