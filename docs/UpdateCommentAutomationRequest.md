

# UpdateCommentAutomationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) |  |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Inline DM buttons (1-3). Pass [] to clear all buttons. |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |



