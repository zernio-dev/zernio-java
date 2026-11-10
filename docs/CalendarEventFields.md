

# CalendarEventFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  [optional] |
|**description** | **String** | HTML. |  [optional] |
|**location** | **String** |  |  [optional] |
|**start** | **String** | ISO date-time, or a date (&#x60;YYYY-MM-DD&#x60;) for all-day events. |  [optional] |
|**end** | **String** | Exclusive for all-day events. |  [optional] |
|**allDay** | **Boolean** |  |  [optional] |
|**timezone** | **String** | IANA zone the event is scheduled in. Defaults to the calendar&#39;s zone on Google and the mailbox&#39;s working-hours zone on Microsoft (UTC when Outlook has none, as on personal accounts). A PATCH that moves an event without a zone keeps the zone the event already has. |  [optional] |
|**participants** | [**List&lt;CalendarEventFieldsParticipantsInner&gt;**](CalendarEventFieldsParticipantsInner.md) |  |  [optional] |
|**recurrence** | **List&lt;String&gt;** | RRULE lines, e.g. &#x60;RRULE:FREQ&#x3D;WEEKLY;BYDAY&#x3D;MO,WE;COUNT&#x3D;10&#x60;. Microsoft takes one RRULE plus EXDATE lines; Zernio removes the EXDATE occurrences after saving the series. |  [optional] |
|**reminders** | [**CalendarEventFieldsReminders**](CalendarEventFieldsReminders.md) |  |  [optional] |
|**conferencing** | [**ConferencingEnum**](#ConferencingEnum) |  |  [optional] |
|**busy** | **Boolean** |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | String pairs stored on the event and returned on reads, on Google and Microsoft. |  [optional] |
|**notifyParticipants** | [**NotifyParticipantsEnum**](#NotifyParticipantsEnum) | Who gets an invitation or update email for this write: everyone, only guests outside the organizer&#39;s domain, or nobody. Google only; Outlook always notifies, so &#x60;external&#x60; and &#x60;none&#x60; answer 400 &#x60;unsupported_for_provider&#x60; on a Microsoft account. |  [optional] |



## Enum: ConferencingEnum

| Name | Value |
|---- | -----|
| GOOGLE_MEET | &quot;google_meet&quot; |
| TEAMS | &quot;teams&quot; |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| PUBLIC | &quot;public&quot; |
| PRIVATE | &quot;private&quot; |



## Enum: NotifyParticipantsEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| EXTERNAL | &quot;external&quot; |
| NONE | &quot;none&quot; |



