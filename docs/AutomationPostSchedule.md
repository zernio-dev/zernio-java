

# AutomationPostSchedule

When a scheduled automation checks its posts. Set times and quiet hours are not available for posts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**every** | [**EveryEnum**](#EveryEnum) |  |  |
|**startsAt** | **OffsetDateTime** | Runs from this time on. |  [optional] |
|**endsAt** | **OffsetDateTime** | Stops running after this time. |  [optional] |



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



