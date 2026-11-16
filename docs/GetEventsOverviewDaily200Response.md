

# GetEventsOverviewDaily200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**period** | [**PeriodEnum**](#PeriodEnum) |  |  [optional] |
|**totals** | [**GetEventsOverviewDaily200ResponseTotals**](GetEventsOverviewDaily200ResponseTotals.md) |  |  [optional] |
|**days** | [**List&lt;GetEventsOverviewDaily200ResponseDaysInner&gt;**](GetEventsOverviewDaily200ResponseDaysInner.md) | Every day of the period, oldest first, zero where nothing happened. |  [optional] |



## Enum: PeriodEnum

| Name | Value |
|---- | -----|
| TODAY | &quot;today&quot; |
| _7D | &quot;7d&quot; |
| _30D | &quot;30d&quot; |



