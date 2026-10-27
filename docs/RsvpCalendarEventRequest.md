

# RsvpCalendarEventRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**calendarId** | **String** | The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**comment** | **String** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |
| DECLINED | &quot;declined&quot; |
| TENTATIVE | &quot;tentative&quot; |



