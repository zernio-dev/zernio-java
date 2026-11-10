

# WebhookPayloadCalendarEventCalendarEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) |  |  [optional] |
|**calendarId** | **String** | The calendar holding the event, to pass as &#x60;calendarId&#x60; when reading it: &#x60;primary&#x60; for the user&#39;s main calendar. Null when it is not known, as for a deleted Outlook event. |  [optional] |
|**masterEventId** | **String** | The series this event belongs to, when it is an occurrence or exception. |  [optional] |



## Enum: ChangeTypeEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;created&quot; |
| UPDATED | &quot;updated&quot; |
| DELETED | &quot;deleted&quot; |



