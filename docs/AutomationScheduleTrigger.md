

# AutomationScheduleTrigger

When an ad rule runs: `every` an interval or at set weekly `times` (send one), optionally only between `startsAt` and `endsAt` and never inside `quietHours`. Times and quiet hours are in the ad account timezone. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**every** | [**EveryEnum**](#EveryEnum) | Run every interval. Send this or &#x60;times&#x60;, not both. |  [optional] |
|**times** | [**List&lt;AutomationScheduleTriggerTimesInner&gt;**](AutomationScheduleTriggerTimesInner.md) | Set weekly times. Send this or &#x60;every&#x60;, not both. |  [optional] |
|**startsAt** | **OffsetDateTime** | Runs from this time on. |  [optional] |
|**endsAt** | **OffsetDateTime** | Stops running after this time. Must be after &#x60;startsAt&#x60;. |  [optional] |
|**quietHours** | [**AutomationScheduleTriggerQuietHours**](AutomationScheduleTriggerQuietHours.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SCHEDULE | &quot;schedule&quot; |



## Enum: EveryEnum

| Name | Value |
|---- | -----|
| _15M | &quot;15m&quot; |
| _30M | &quot;30m&quot; |
| _1H | &quot;1h&quot; |
| _3H | &quot;3h&quot; |
| _6H | &quot;6h&quot; |
| _12H | &quot;12h&quot; |
| _1D | &quot;1d&quot; |



