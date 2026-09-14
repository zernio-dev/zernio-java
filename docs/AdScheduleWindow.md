

# AdScheduleWindow

One ad schedule window as Google stores it. Half-open: it is exclusive of the end minute, so 09:00-12:00 and 12:00-17:00 are adjacent, not overlapping.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**criterionId** | **String** | Google campaign criterion id. Changes whenever the window is rewritten, because Google cannot edit a schedule in place. |  [optional] |
|**resourceName** | **String** |  |  [optional] |
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) |  |  [optional] |
|**startHour** | **Integer** |  |  [optional] |
|**startMinute** | [**StartMinuteEnum**](#StartMinuteEnum) |  |  [optional] |
|**endHour** | **Integer** | 24 means midnight at the end of the day. |  [optional] |
|**endMinute** | [**EndMinuteEnum**](#EndMinuteEnum) |  |  [optional] |
|**bidModifier** | **BigDecimal** | Bid adjustment for this window, 0.1-10.0. Null when the window runs at the campaign bid. |  [optional] |



## Enum: DayOfWeekEnum

| Name | Value |
|---- | -----|
| MONDAY | &quot;MONDAY&quot; |
| TUESDAY | &quot;TUESDAY&quot; |
| WEDNESDAY | &quot;WEDNESDAY&quot; |
| THURSDAY | &quot;THURSDAY&quot; |
| FRIDAY | &quot;FRIDAY&quot; |
| SATURDAY | &quot;SATURDAY&quot; |
| SUNDAY | &quot;SUNDAY&quot; |



## Enum: StartMinuteEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_15 | 15 |
| NUMBER_30 | 30 |
| NUMBER_45 | 45 |



## Enum: EndMinuteEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_15 | 15 |
| NUMBER_30 | 30 |
| NUMBER_45 | 45 |



