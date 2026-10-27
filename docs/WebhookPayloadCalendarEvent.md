

# WebhookPayloadCalendarEvent

Webhook payload for calendar.event.created, calendar.event.updated and calendar.event.deleted. Carries the provider event id and the change only; read the event with `GET /v1/calendar/events/{id}` (deleted ids answer 404).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Present on every event tied to a profile and absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once. Use it to route the event to your tenant without storing Zernio profile ids. |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadCalendarEventAccount**](WebhookPayloadCalendarEventAccount.md) |  |  |
|**calendarEvent** | [**WebhookPayloadCalendarEventCalendarEvent**](WebhookPayloadCalendarEventCalendarEvent.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CALENDAR_EVENT_CREATED | &quot;calendar.event.created&quot; |
| CALENDAR_EVENT_UPDATED | &quot;calendar.event.updated&quot; |
| CALENDAR_EVENT_DELETED | &quot;calendar.event.deleted&quot; |



