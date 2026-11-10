

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
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;series&#x60; is a recurring master, &#x60;occurrence&#x60; one of its instances, and &#x60;exception&#x60; an instance changed on its own. Google flags an instance as an exception only when it was moved off its slot. |  [optional] |
|**originalStart** | **String** | For an occurrence or exception, the start it has in the series pattern. |  [optional] |
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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |
| SERIES | &quot;series&quot; |
| OCCURRENCE | &quot;occurrence&quot; |
| EXCEPTION | &quot;exception&quot; |



