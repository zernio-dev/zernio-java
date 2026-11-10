

# CalendarFreeBusy200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**from** | **OffsetDateTime** |  |  [optional] |
|**to** | **OffsetDateTime** |  |  [optional] |
|**busy** | [**List&lt;BusyBlock&gt;**](BusyBlock.md) | The account&#39;s own busy time across the calendars read, merged. Null when the account could not be read. |  [optional] |
|**calendars** | [**List&lt;CalendarFreeBusy200ResponseDataInnerCalendarsInner&gt;**](CalendarFreeBusy200ResponseDataInnerCalendarsInner.md) |  |  [optional] |
|**people** | [**List&lt;CalendarFreeBusy200ResponseDataInnerPeopleInner&gt;**](CalendarFreeBusy200ResponseDataInnerPeopleInner.md) |  |  [optional] |
|**error** | [**FreeBusyError**](FreeBusyError.md) |  |  [optional] |



