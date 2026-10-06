

# CommentAutomationLog


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**commentId** | **String** |  |  [optional] |
|**commenterId** | **String** |  |  [optional] |
|**commenterName** | **String** |  |  [optional] |
|**commenterUsername** | **String** |  |  [optional] |
|**commentText** | **String** |  |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | Which door triggered this send. Null on rows written before this field existed (all of those are comment-triggered). |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | DM outcome. &#39;pending&#39; &#x3D; the automation has a dmDelaySeconds and the response is queued but not sent yet. &#39;gated&#39; &#x3D; the follow-gate confirmation DM went out and we are waiting for the tap; it flips to &#39;sent&#39; or &#39;skipped&#39; when they tap. &#39;skipped&#39; also covers repeatPolicy, cooldown and dedupeSameTextHours suppressions, with the reason in error. |  [optional] |
|**audienceOutcome** | [**AudienceOutcomeEnum**](#AudienceOutcomeEnum) | How the audience rule resolved. Null on automations without one. |  [optional] |
|**gateButtonStatus** | [**GateButtonStatusEnum**](#GateButtonStatusEnum) | Whether the follow-gate button reached the commenter: &#39;rejected&#39; &#x3D; Meta refused the gate DM, &#39;omitted&#39; &#x3D; the prompt went out as plain text because it was over 640 characters. Null when no gate DM was sent. |  [optional] |
|**commenterIsFollower** | **Boolean** | Follow relationship at decision time. Null when Instagram would not tell us (the commenter never messaged the account). |  [optional] |
|**commenterFollowerCount** | **Integer** |  |  [optional] |
|**gateResolvedAt** | **OffsetDateTime** | When the follow-gate tap was claimed. |  [optional] |
|**error** | **String** | DM error message when status is failed, or the reason when it is skipped. |  [optional] |
|**platformError** | [**CommentAutomationLogPlatformError**](CommentAutomationLogPlatformError.md) |  |  [optional] |
|**privateReplyConsumed** | **Boolean** | True when the failed send spent the comment&#39;s single private reply (Instagram subcode 1545133 or 2534023, or Meta code 10900 on Instagram and Facebook), the same rule as &#x60;details.privateReplyConsumed&#x60; on the private-reply endpoint. Null on direct DMs and on rows written before this field existed. |  [optional] |
|**commentReplyStatus** | [**CommentReplyStatusEnum**](#CommentReplyStatusEnum) | Outcome of the optional public reply on the triggering comment. With publicReplyPolicy after_dm, &#39;skipped&#39; if no commentReply was configured or if the DM failed (the public reply is not attempted in that case). |  [optional] |
|**commentReplyError** | **String** | Public-reply error message if commentReplyStatus is failed |  [optional] |
|**publicReplyPostedAt** | **OffsetDateTime** | When the public reply was posted. Null when it was not. |  [optional] |
|**likeSkipped** | **String** | Why actions.likeComment did not like the comment. Null when it did or was not configured. |  [optional] |
|**hideSkipped** | **String** | Why actions.hideComment did not hide the comment. Null when it did or was not configured. |  [optional] |
|**mediaError** | **String** | Why the dmMedia follow-up was not delivered. The DM itself still counts as sent. |  [optional] |
|**nextDueAt** | **OffsetDateTime** | When the next queued send fires. Present only while something is still pending. |  [optional] |
|**clickedAt** | **OffsetDateTime** | This recipient&#39;s first click on a tracked link (what uniqueClicks counts). |  [optional] |
|**clickCount** | **Integer** | This recipient&#39;s total clicks on tracked links. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| COMMENT | &quot;comment&quot; |
| LIVE_COMMENT | &quot;live_comment&quot; |
| STORY_REPLY | &quot;story_reply&quot; |
| STORY_MENTION | &quot;story_mention&quot; |
| DM | &quot;dm&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |
| GATED | &quot;gated&quot; |



## Enum: AudienceOutcomeEnum

| Name | Value |
|---- | -----|
| PASSED | &quot;passed&quot; |
| BLOCKED | &quot;blocked&quot; |
| GATE_SENT | &quot;gate_sent&quot; |
| GATE_PASSED | &quot;gate_passed&quot; |
| GATE_FAILED | &quot;gate_failed&quot; |



## Enum: GateButtonStatusEnum

| Name | Value |
|---- | -----|
| DELIVERED | &quot;delivered&quot; |
| REJECTED | &quot;rejected&quot; |
| OMITTED | &quot;omitted&quot; |



## Enum: CommentReplyStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |



