

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
|**timezone** | **String** | IANA zone the event is scheduled in. Default UTC. |  [optional] |
|**participants** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**recurrence** | **List&lt;String&gt;** | RRULE lines, e.g. &#x60;RRULE:FREQ&#x3D;WEEKLY;BYDAY&#x3D;MO,WE;COUNT&#x3D;10&#x60;. |  [optional] |
|**reminders** | [**CalendarEventFieldsReminders**](CalendarEventFieldsReminders.md) |  |  [optional] |
|**conferencing** | [**ConferencingEnum**](#ConferencingEnum) |  |  [optional] |
|**busy** | **Boolean** |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |



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



