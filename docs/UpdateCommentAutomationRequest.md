

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
|**dmMessageVariations** | **List&lt;String&gt;** | Alternate DM texts for random rotation (see create). Pass [] to clear. |  [optional] |
|**commentReplyVariations** | **List&lt;String&gt;** | Alternate public replies for random rotation. Pass [] to clear. |  [optional] |
|**linkTracking** | **Boolean** | Wrap link buttons in a tracked redirect to count clicks. Pass false to send links untouched. |  [optional] |
|**clickTag** | **String** | Tag applied to a contact when they click a tracked link (requires linkTracking). Empty string clears it. |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |



