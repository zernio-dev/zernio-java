

# UpdateCommentAutomation200ResponseAutomation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) |  |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Inline DM buttons (up to 3). Omitted when none are set. |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |



