

# GetCommentAutomation200ResponseAutomation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platformPostId** | **String** |  |  [optional] |
|**postId** | **String** |  |  [optional] |
|**postTitle** | **String** |  |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) |  |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Inline DM buttons (up to 3). Omitted when none are set. |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**linkTracking** | **Boolean** |  |  [optional] |
|**clickTag** | **String** |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**stats** | [**CreateCommentAutomation200ResponseAutomationStats**](CreateCommentAutomation200ResponseAutomationStats.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| COMMENT | &quot;comment&quot; |
| STORY_REPLY | &quot;story_reply&quot; |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |



