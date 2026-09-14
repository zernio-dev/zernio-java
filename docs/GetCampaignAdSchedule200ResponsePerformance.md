

# GetCampaignAdSchedule200ResponsePerformance

Only present when includePerformance=true.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**windowDays** | **Integer** | The trailing window used, or null when an explicit fromDate/toDate range was given. |  [optional] |
|**byDayOfWeek** | [**List&lt;GetCampaignAdSchedule200ResponsePerformanceByDayOfWeekInner&gt;**](GetCampaignAdSchedule200ResponsePerformanceByDayOfWeekInner.md) | One entry per day that delivered, Monday first. |  [optional] |
|**byHour** | [**List&lt;GetCampaignAdSchedule200ResponsePerformanceByHourInner&gt;**](GetCampaignAdSchedule200ResponsePerformanceByHourInner.md) | One entry per hour that delivered, 0-23 in the account time zone. |  [optional] |



