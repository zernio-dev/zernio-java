

# FollowerStatsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | [**List&lt;AccountWithFollowerStats&gt;**](AccountWithFollowerStats.md) |  |  [optional] |
|**stats** | **Map&lt;String, List&lt;FollowerStatsResponseStatsValueInner&gt;&gt;** |  |  [optional] |
|**dateRange** | [**FollowerStatsResponseDateRange**](FollowerStatsResponseDateRange.md) |  |  [optional] |
|**granularity** | **String** |  |  [optional] |
|**pagination** | [**AccountCursorPagination**](AccountCursorPagination.md) | Present when limit or cursor is sent, and on the default page of 25 that an API request without accountIds gets. |  [optional] |
|**warning** | **String** | Only when the response was cut: the default page of 25 accounts (page through the rest with cursor), or a date range longer than a year (dateRange.from shows where the data starts). Both reasons are joined when they apply together. |  [optional] |



