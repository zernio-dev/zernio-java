

# UpdateCommentAutomationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | What fires the automation. Changing it detaches the automation from its bound post or story (a post id and a story id are different objects), unless this same request sets a new binding. &#39;story_reply&#39; is Instagram only. |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) | How a keyword is compared with the comment. &#39;contains&#39; (default) matches anywhere, even inside another word (keyword &#39;app&#39; fires on &#39;happy&#39;). &#39;word&#39; matches the keyword only as a standalone word. &#39;exact&#39; requires the whole comment to be exactly the keyword. |  [optional] |
|**excludeKeywords** | **List&lt;String&gt;** | Comments containing one of these never trigger the automation, even when a trigger keyword also matches. Compared using the same matchMode. |  [optional] |
|**typoTolerance** | **Boolean** | Only with matchMode&#x3D;word: also fire on close misspellings of a keyword (one edit for 4-7 character keywords, two from 8 up). Keywords shorter than 4 characters are never fuzzy-matched. |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Inline DM buttons (1-3). Pass [] to clear all buttons. |  [optional] |
|**template** | [**CommentAutomationTemplate**](CommentAutomationTemplate.md) |  |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**dmMessageVariations** | **List&lt;String&gt;** | Alternate DM texts for random rotation (see create). Pass [] to clear. |  [optional] |
|**commentReplyVariations** | **List&lt;String&gt;** | Alternate public replies for random rotation. Pass [] to clear. |  [optional] |
|**linkTracking** | **Boolean** | Wrap link buttons in a tracked redirect to count clicks. Pass false to send links untouched. |  [optional] |
|**clickTag** | **String** | Tag applied to a contact when they click a tracked link (requires linkTracking). Empty string clears it. |  [optional] |
|**dmDelaySeconds** | **Integer** | Seconds to wait after the trigger before sending the DM. Send 0 to clear the delay and reply immediately. |  [optional] |
|**commentReplyDelaySeconds** | **Integer** | Seconds to wait before posting the public comment reply. Send 0 to clear it. The reply never goes out before the DM. |  [optional] |
|**audience** | [**CommentAutomationAudience**](CommentAutomationAudience.md) |  |  [optional] |
|**followGate** | [**CommentAutomationFollowGate**](CommentAutomationFollowGate.md) |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |



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
| WORD | &quot;word&quot; |



