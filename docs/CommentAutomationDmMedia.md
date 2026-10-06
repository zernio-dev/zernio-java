

# CommentAutomationDmMedia

An image, video, audio clip or file sent right after the DM text as a second message (a Meta message carries one body, so text and attachment are two sends). On the comment trigger Meta may refuse the second message until the commenter replies; the DM then still counts as sent and the log row carries `mediaError`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**url** | **URI** | Publicly reachable http(s) URL Meta downloads the media from. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| AUDIO | &quot;audio&quot; |
| FILE | &quot;file&quot; |



