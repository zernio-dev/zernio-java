

# GetAnalyticsDashboard200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateRange** | [**GetAnalyticsDashboard200ResponseDateRange**](GetAnalyticsDashboard200ResponseDateRange.md) |  |  |
|**totals** | [**AnalyticsDashboardTotals**](AnalyticsDashboardTotals.md) |  |  |
|**previousTotals** | [**AnalyticsDashboardTotals**](AnalyticsDashboardTotals.md) |  |  [optional] |
|**followers** | [**AnalyticsDashboardFollowers**](AnalyticsDashboardFollowers.md) |  |  |
|**previousFollowers** | [**AnalyticsDashboardFollowers**](AnalyticsDashboardFollowers.md) |  |  [optional] |
|**daily** | [**List&lt;GetAnalyticsDashboard200ResponseDailyInner&gt;**](GetAnalyticsDashboard200ResponseDailyInner.md) | One entry per day of the window, days without data included as zeros. |  |
|**topPosts** | [**List&lt;AnalyticsDashboardPost&gt;**](AnalyticsDashboardPost.md) |  |  |
|**recentPosts** | [**List&lt;AnalyticsDashboardPost&gt;**](AnalyticsDashboardPost.md) |  |  |
|**dataAsOf** | **OffsetDateTime** | When the most recently synced account in scope was last synced. Null if none has synced yet. |  |



