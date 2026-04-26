

# GetCommentAutomation200ResponseLogsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**commentId** | **String** |  |  [optional] |
|**commenterId** | **String** |  |  [optional] |
|**commenterName** | **String** |  |  [optional] |
|**commentText** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | DM outcome |  [optional] |
|**error** | **String** | DM error message if status is failed |  [optional] |
|**commentReplyStatus** | [**CommentReplyStatusEnum**](#CommentReplyStatusEnum) | Outcome of the optional public reply on the triggering comment. &#39;skipped&#39; if no commentReply was configured or if the DM failed (the public reply is not attempted in that case). |  [optional] |
|**commentReplyError** | **String** | Public-reply error message if commentReplyStatus is failed |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |



## Enum: CommentReplyStatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |



