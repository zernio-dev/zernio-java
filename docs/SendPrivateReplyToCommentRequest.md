

# SendPrivateReplyToCommentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The social account ID (Instagram or Facebook) |  |
|**message** | **String** | The message text to send as a private DM |  |
|**quickReplies** | [**List&lt;SendPrivateReplyToCommentRequestQuickRepliesInner&gt;**](SendPrivateReplyToCommentRequestQuickRepliesInner.md) | Optional quick-reply chips appended to the message. Visible only in the Instagram and Messenger apps (not on web). Maximum 13 entries. Mutually exclusive with &#x60;buttons&#x60;. Note: chips do NOT render in the Instagram Message Requests folder where DMs from non-followers land — use &#x60;buttons&#x60; instead for cold reach.  |  [optional] |
|**buttons** | [**List&lt;SendPrivateReplyToCommentRequestButtonsInner&gt;**](SendPrivateReplyToCommentRequestButtonsInner.md) | Optional 1-3 inline buttons rendered as part of the same message bubble via Meta&#39;s button_template. Visible in the Instagram Message Requests folder (unlike quick replies). Mutually exclusive with &#x60;quickReplies&#x60;.  |  [optional] |



