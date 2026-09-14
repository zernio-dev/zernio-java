

# UpdateCampaignAdScheduleRequestScheduleInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) |  |  |
|**startHour** | **Integer** |  |  |
|**startMinute** | [**StartMinuteEnum**](#StartMinuteEnum) | Quarter-hours only. |  [optional] |
|**endHour** | **Integer** | 24 means midnight at the end of the day. |  |
|**endMinute** | [**EndMinuteEnum**](#EndMinuteEnum) | Quarter-hours only. Must be 0 when endHour is 24. |  [optional] |
|**bidModifier** | **BigDecimal** | Bid adjustment for this window. Null runs it at the campaign bid. |  [optional] |



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



