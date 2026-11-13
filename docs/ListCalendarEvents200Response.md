

# ListCalendarEvents200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;CalendarEvent&gt;**](CalendarEvent.md) |  |  [optional] |
|**pagination** | [**CursorPagination**](CursorPagination.md) |  |  [optional] |
|**stale** | **Boolean** | Always true when present. Present only when the provider did not answer and this is the last list Zernio read for the same account and query within the past six hours. |  [optional] |
|**asOf** | **OffsetDateTime** | When a stale list was read from the provider. Present only with &#x60;stale&#x60;. |  [optional] |
|**partial** | **Boolean** | Always true when present. This response is one slice of the requested window because the provider did not answer for the whole of it. Follow &#x60;pagination.nextCursor&#x60; until it is null. Present only on a degraded read. |  [optional] |
|**coveredFrom** | **OffsetDateTime** | Start of the part of the window this slice covers. Present only with &#x60;partial&#x60;. |  [optional] |
|**coveredTo** | **OffsetDateTime** | End of the part of the window this slice covers. Present only with &#x60;partial&#x60;. |  [optional] |



