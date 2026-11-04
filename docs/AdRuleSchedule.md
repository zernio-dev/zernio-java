

# AdRuleSchedule

Either `everyMinutes` or `times`. Sending a schedule replaces the rule's whole timing. Without one, a new rule runs every 60 minutes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**everyMinutes** | [**EveryMinutesEnum**](#EveryMinutesEnum) | How often the rule runs, in minutes. Null on a rule that runs at set times. |  [optional] |
|**times** | [**List&lt;AdRuleScheduleTimesInner&gt;**](AdRuleScheduleTimesInner.md) | Set weekly times in the ad account timezone, instead of an interval. A rule that changes ads needs a cooldown of at least the shortest gap between two times. |  [optional] |
|**startsAt** | **OffsetDateTime** | The rule runs from this time on. |  [optional] |
|**endsAt** | **OffsetDateTime** | The rule stops running after this time. |  [optional] |



## Enum: EveryMinutesEnum

| Name | Value |
|---- | -----|
| NUMBER_15 | 15 |
| NUMBER_30 | 30 |
| NUMBER_60 | 60 |
| NUMBER_180 | 180 |
| NUMBER_360 | 360 |
| NUMBER_720 | 720 |
| NUMBER_1440 | 1440 |



