

# ListCalendarEvents200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;CalendarEvent&gt;**](CalendarEvent.md) |  |  [optional] |
|**pagination** | [**CursorPagination**](CursorPagination.md) |  |  [optional] |
|**stale** | **Boolean** | Always true when present. Present only when the provider did not answer and this is the last list Zernio read for the same account and query within the past hour. |  [optional] |
|**asOf** | **OffsetDateTime** | When a stale list was read from the provider. Present only with &#x60;stale&#x60;. |  [optional] |



