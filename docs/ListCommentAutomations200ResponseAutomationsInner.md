

# ListCommentAutomations200ResponseAutomationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platformPostId** | **String** |  |  [optional] |
|**postTitle** | **String** |  |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) |  |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Inline DM buttons (up to 3). Omitted when none are set. |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**stats** | [**ListCommentAutomations200ResponseAutomationsInnerStats**](ListCommentAutomations200ResponseAutomationsInnerStats.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |



