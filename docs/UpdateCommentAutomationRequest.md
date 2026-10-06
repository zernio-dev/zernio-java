

# UpdateCommentAutomationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | What fires the automation. Changing it detaches the automation from its bound post or story (a post id and a story id are different objects), unless this same request sets a new binding. Every trigger but &#39;comment&#39; is Instagram only; &#39;story_mention&#39; also requires no keywords and no binding. |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) | How a keyword is compared with the comment. &#39;contains&#39; (default) matches anywhere, even inside another word (keyword &#39;app&#39; fires on &#39;happy&#39;). &#39;word&#39; matches the keyword only as a standalone word. &#39;exact&#39; requires the whole comment to be exactly the keyword. |  [optional] |
|**excludeKeywords** | **List&lt;String&gt;** | Comments containing one of these never trigger the automation, even when a trigger keyword also matches. Compared using the same matchMode. |  [optional] |
|**typoTolerance** | **Boolean** | Only with matchMode&#x3D;word: also fire on close misspellings of a keyword (one edit for 4-7 character keywords, two from 8 up). Keywords shorter than 4 characters are never fuzzy-matched. |  [optional] |
|**platformPostId** | **String** | Re-binds the automation to another post: the platform media/post ID (or story media id when trigger&#x3D;story_reply). postId, platformPostId and postTitle move as a unit: sending any of them replaces all three, and an omitted one is cleared. Send all three as null (or empty) to make it account-wide (any post / any story). Omit all three to keep the current binding. 409 when another active automation already owns the new post. |  [optional] |
|**postId** | **String** | Zernio post ID (24 hexadecimal characters); platform IDs return 400. Use it INSTEAD of platformPostId to bind to a not-yet-published Zernio post: the automation stays pending and arms itself when that post publishes. Moves as a unit with platformPostId and postTitle (see platformPostId). |  [optional] |
|**postTitle** | **String** | Post content snippet for display. Moves as a unit with platformPostId and postId (see platformPostId). |  [optional] |
|**dmMessage** | **String** |  |  [optional] |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Inline DM buttons (1-3). Pass [] to clear all buttons. |  [optional] |
|**template** | [**CommentAutomationTemplate**](CommentAutomationTemplate.md) |  |  [optional] |
|**commentReply** | **String** |  |  [optional] |
|**dmMessageVariations** | **List&lt;String&gt;** | Alternate DM texts for random rotation (see create). Pass [] to clear. |  [optional] |
|**commentReplyVariations** | **List&lt;String&gt;** | Alternate public replies for random rotation. Pass [] to clear. |  [optional] |
|**linkTracking** | **Boolean** | Wrap link buttons in a tracked redirect to count clicks. Pass false to send links untouched. |  [optional] |
|**clickTag** | **String** | Tag applied to a contact when they click a tracked link (requires linkTracking). Empty string clears it. |  [optional] |
|**alsoMatchInDms** | **Boolean** | Also fire these keywords on a plain inbound DM. Enabling it requires the automation to end up with at least one keyword (this request&#39;s keywords if you send them, otherwise the stored ones) and is rejected on story_reply automations. |  [optional] |
|**dmDelaySeconds** | **Integer** | Seconds to wait after the trigger before sending the DM. Send 0 to clear the delay and reply immediately. |  [optional] |
|**commentReplyDelaySeconds** | **Integer** | Seconds to wait before posting the public comment reply. Send 0 to clear it. The reply never goes out before the DM. |  [optional] |
|**audience** | [**CommentAutomationAudience**](CommentAutomationAudience.md) |  |  [optional] |
|**followGate** | [**CommentAutomationFollowGate**](CommentAutomationFollowGate.md) |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**repeatPolicy** | [**CommentAutomationRepeatPolicy**](CommentAutomationRepeatPolicy.md) |  |  [optional] |
|**dedupeSameTextHours** | **Integer** | Skip the DM when this recipient already received identical DM text (after personalisation) from this account, from any automation, within this many hours. The skip is logged with status skipped. Send null to clear. |  [optional] |
|**publicReplyPolicy** | [**PublicReplyPolicyEnum**](#PublicReplyPolicyEnum) | &#39;after_dm&#39; posts commentReply only after a successful DM. &#39;always&#39; posts it whatever the audience rule, dedupe or DM outcome: the moment a comment matches, or after commentReplyDelaySeconds when set (raised to dmDelaySeconds, so it never precedes the DM attempt). |  [optional] |
|**actions** | [**CommentAutomationActions**](CommentAutomationActions.md) |  |  [optional] |
|**quickReplies** | [**List&lt;CommentAutomationQuickReply&gt;**](CommentAutomationQuickReply.md) | Opt-in quick-reply chips on the DM (up to 13). Chips do not render in Message Requests, where a first DM to a cold commenter lands, so prefer buttons for first contact. Mutually exclusive with buttons and template (400). Send null to clear. |  [optional] |
|**dmMedia** | [**CommentAutomationDmMedia**](CommentAutomationDmMedia.md) |  |  [optional] |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| COMMENT | &quot;comment&quot; |
| LIVE_COMMENT | &quot;live_comment&quot; |
| STORY_REPLY | &quot;story_reply&quot; |
| STORY_MENTION | &quot;story_mention&quot; |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |
| WORD | &quot;word&quot; |



## Enum: PublicReplyPolicyEnum

| Name | Value |
|---- | -----|
| AFTER_DM | &quot;after_dm&quot; |
| ALWAYS | &quot;always&quot; |



