

# GetCommentAutomation200ResponseLogsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**commentId** | **String** |  |  [optional] |
|**commenterId** | **String** |  |  [optional] |
|**commenterName** | **String** |  |  [optional] |
|**commentText** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | DM outcome. &#39;pending&#39; &#x3D; the automation has a dmDelaySeconds and the response is queued but not sent yet. &#39;gated&#39; &#x3D; the follow-gate confirmation DM went out and we are waiting for the tap; it flips to &#39;sent&#39; or &#39;skipped&#39; when they tap. |  [optional] |
|**audienceOutcome** | [**AudienceOutcomeEnum**](#AudienceOutcomeEnum) | How the audience rule resolved. Absent on automations without one. |  [optional] |
|**commenterIsFollower** | **Boolean** | Follow relationship at decision time. Absent when Instagram would not tell us (the commenter never messaged the account). |  [optional] |
|**commenterFollowerCount** | **Integer** |  |  [optional] |
|**error** | **String** | DM error message if status is failed |  [optional] |
|**commentReplyStatus** | [**CommentReplyStatusEnum**](#CommentReplyStatusEnum) | Outcome of the optional public reply on the triggering comment. &#39;skipped&#39; if no commentReply was configured or if the DM failed (the public reply is not attempted in that case). |  [optional] |
|**commentReplyError** | **String** | Public-reply error message if commentReplyStatus is failed |  [optional] |
|**nextDueAt** | **OffsetDateTime** | When the next queued send fires. Present only while something is still pending. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



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



## Enum: CommentReplyStatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |



