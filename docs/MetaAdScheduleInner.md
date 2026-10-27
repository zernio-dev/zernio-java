

# MetaAdScheduleInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) |  |  |
|**startHour** | **Integer** |  |  |
|**endHour** | **Integer** | Must be after startHour. 24 is midnight at the end of the day. |  |
|**timezoneType** | [**TimezoneTypeEnum**](#TimezoneTypeEnum) | Meta &#x60;timezone_type&#x60;: USER runs the hours in each viewer&#39;s time zone, ADVERTISER in the ad account time zone. |  [optional] |



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



## Enum: TimezoneTypeEnum

| Name | Value |
|---- | -----|
| USER | &quot;USER&quot; |
| ADVERTISER | &quot;ADVERTISER&quot; |



