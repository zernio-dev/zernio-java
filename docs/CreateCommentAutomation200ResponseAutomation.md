

# CreateCommentAutomation200ResponseAutomation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**platformPostId** | **String** |  |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) |  |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**stats** | [**CreateCommentAutomation200ResponseAutomationStats**](CreateCommentAutomation200ResponseAutomationStats.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |



