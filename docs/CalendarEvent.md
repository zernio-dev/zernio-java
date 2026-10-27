

# CalendarEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) |  |  [optional] |
|**calendarId** | **String** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**location** | **String** |  |  [optional] |
|**start** | **String** | ISO date-time with the rendered offset, or a date for all-day events. |  [optional] |
|**end** | **String** |  |  [optional] |
|**allDay** | **Boolean** |  |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**participants** | [**List&lt;CalendarEventParticipantsInner&gt;**](CalendarEventParticipantsInner.md) |  |  [optional] |
|**organizer** | [**EmailAddress**](EmailAddress.md) |  |  [optional] |
|**recurrence** | **List&lt;String&gt;** |  |  [optional] |
|**reminders** | [**CalendarEventReminders**](CalendarEventReminders.md) |  |  [optional] |
|**conferencing** | [**CalendarEventConferencing**](CalendarEventConferencing.md) |  |  [optional] |
|**busy** | **Boolean** |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**icalUid** | **String** |  |  [optional] |
|**masterEventId** | **String** |  |  [optional] |
|**htmlLink** | **String** |  |  [optional] |
|**readOnly** | **Boolean** |  |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| PUBLIC | &quot;public&quot; |
| PRIVATE | &quot;private&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CONFIRMED | &quot;confirmed&quot; |
| TENTATIVE | &quot;tentative&quot; |
| CANCELLED | &quot;cancelled&quot; |



