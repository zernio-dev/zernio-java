

# CommentAutomationRepeatPolicy

Whether a commenter can receive this automation's DM more than once.   * `once` (default) - one DM per person per door, ever.   * `every_comment` - every new matching comment is eligible again. One comment     is still answered at most once. `cooldownHours` suppresses a repeat sent to the     same person within that many hours. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) |  |  |
|**cooldownHours** | **Integer** | every_comment only (400 with once). Hours after a DM during which the same person is not DMed again. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ONCE | &quot;once&quot; |
| EVERY_COMMENT | &quot;every_comment&quot; |



