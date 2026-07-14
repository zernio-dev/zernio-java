

# ListCommentAutomations200ResponseAutomationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platformPostId** | **String** |  |  [optional] |
|**postTitle** | **String** |  |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) |  |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Inline DM buttons (up to 3). Omitted when none are set. |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**dmMessageVariations** | **List&lt;String&gt;** | Alternate DM texts rotated at random with dmMessage. Omitted when none. |  [optional] |
|**commentReplyVariations** | **List&lt;String&gt;** | Alternate public replies rotated at random with commentReply. Omitted when none. |  [optional] |
|**linkTracking** | **Boolean** | Whether link buttons in the DM are wrapped in a tracked redirect to count clicks. |  [optional] |
|**clickTag** | **String** | Tag applied to a contact when they click a tracked link. |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**stats** | [**ListCommentAutomations200ResponseAutomationsInnerStats**](ListCommentAutomations200ResponseAutomationsInnerStats.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |



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



