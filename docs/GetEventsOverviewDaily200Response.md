

# GetEventsOverviewDaily200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**period** | [**PeriodEnum**](#PeriodEnum) |  |  [optional] |
|**totals** | [**GetEventsOverviewDaily200ResponseTotals**](GetEventsOverviewDaily200ResponseTotals.md) |  |  [optional] |
|**days** | [**List&lt;GetEventsOverviewDaily200ResponseDaysInner&gt;**](GetEventsOverviewDaily200ResponseDaysInner.md) | Every day of the period, oldest first, zero where nothing happened. |  [optional] |
|**eventNames** | **List&lt;String&gt;** | The event names stored in the period, most events first. |  [optional] |
|**platforms** | [**List&lt;GetEventsOverviewDaily200ResponsePlatformsInner&gt;**](GetEventsOverviewDaily200ResponsePlatformsInner.md) | Each platform events were sent to in the period, most sends first. |  [optional] |
|**pixelMissed** | [**List&lt;GetEventsOverviewDaily200ResponsePixelMissedInner&gt;**](GetEventsOverviewDaily200ResponsePixelMissedInner.md) | For each platform sent to in the period, the website conversions of people who allowed ad cookies (bots left out) and how many its browser pixel missed, which Zernio sent from its server. Most missed first; &#x60;null&#x60; without a tracked website in scope. |  [optional] |
|**breakdown** | [**GetEventsOverviewDaily200ResponseBreakdown**](GetEventsOverviewDaily200ResponseBreakdown.md) |  |  [optional] |
|**previous** | [**GetEventsOverviewDaily200ResponsePrevious**](GetEventsOverviewDaily200ResponsePrevious.md) |  |  [optional] |



## Enum: PeriodEnum

| Name | Value |
|---- | -----|
| TODAY | &quot;today&quot; |
| _7D | &quot;7d&quot; |
| _30D | &quot;30d&quot; |
| _90D | &quot;90d&quot; |



