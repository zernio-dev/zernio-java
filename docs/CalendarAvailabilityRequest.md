

# CalendarAvailabilityRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**participants** | [**List&lt;CalendarAvailabilityRequestParticipantsInner&gt;**](CalendarAvailabilityRequestParticipantsInner.md) |  |  |
|**from** | **OffsetDateTime** |  |  |
|**to** | **OffsetDateTime** |  |  |
|**durationMinutes** | **Integer** |  |  |
|**intervalMinutes** | **Integer** |  |  [optional] |
|**roundTo** | **Integer** | Rounds the first candidate slot up to this many minutes. |  [optional] |
|**buffer** | [**CalendarAvailabilityRequestBuffer**](CalendarAvailabilityRequestBuffer.md) |  |  [optional] |
|**defaultOpenHours** | [**List&lt;OpenHoursInner&gt;**](OpenHoursInner.md) |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| COLLECTIVE | &quot;collective&quot; |
| MAX_AVAILABILITY | &quot;max_availability&quot; |



