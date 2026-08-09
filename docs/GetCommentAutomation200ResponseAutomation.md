

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
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) | How a keyword is compared with the comment. &#39;contains&#39; (default) matches anywhere, even inside another word (keyword &#39;app&#39; fires on &#39;happy&#39;). &#39;word&#39; matches the keyword only as a standalone word. &#39;exact&#39; requires the whole comment to be exactly the keyword. |  [optional] |
|**excludeKeywords** | **List&lt;String&gt;** | Comments containing one of these never trigger the automation, even when a trigger keyword also matches. Compared using the same matchMode. |  [optional] |
|**typoTolerance** | **Boolean** | Only with matchMode&#x3D;word: also fire on close misspellings of a keyword (one edit for 4-7 character keywords, two from 8 up). Keywords shorter than 4 characters are never fuzzy-matched. |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Inline DM buttons (up to 3). Omitted when none are set. |  [optional] |
|**template** | [**CommentAutomationTemplate**](CommentAutomationTemplate.md) |  |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**dmMessageVariations** | **List&lt;String&gt;** | Alternate DM texts rotated at random with dmMessage. Omitted when none. |  [optional] |
|**commentReplyVariations** | **List&lt;String&gt;** | Alternate public replies rotated at random with commentReply. Omitted when none. |  [optional] |
|**linkTracking** | **Boolean** |  |  [optional] |
|**clickTag** | **String** |  |  [optional] |
|**dmDelaySeconds** | **Integer** | Seconds waited after the trigger before the DM is sent. Absent when the DM goes out immediately. |  [optional] |
|**commentReplyDelaySeconds** | **Integer** | Seconds waited before the public reply is posted. Absent when it follows the DM immediately. |  [optional] |
|**audience** | [**CommentAutomationAudience**](CommentAutomationAudience.md) |  |  [optional] |
|**followGate** | [**CommentAutomationFollowGate**](CommentAutomationFollowGate.md) |  |  [optional] |
|**alsoMatchInDms** | **Boolean** | Whether these keywords also fire on a plain inbound DM. |  [optional] |
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
| WORD | &quot;word&quot; |



