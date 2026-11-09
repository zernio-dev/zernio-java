

# FollowerStatsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | [**List&lt;AccountWithFollowerStats&gt;**](AccountWithFollowerStats.md) |  |  [optional] |
|**stats** | **Map&lt;String, List&lt;FollowerStatsResponseStatsValueInner&gt;&gt;** |  |  [optional] |
|**dateRange** | [**FollowerStatsResponseDateRange**](FollowerStatsResponseDateRange.md) |  |  [optional] |
|**granularity** | **String** |  |  [optional] |
|**pagination** | [**AccountCursorPagination**](AccountCursorPagination.md) | Present when limit or cursor is sent, and on the default page of 25 that an API request without accountIds gets. |  [optional] |
|**warning** | **String** | Only when the default page of 25 cut the list. Page through the rest with cursor. |  [optional] |



