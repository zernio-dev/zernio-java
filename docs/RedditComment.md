

# RedditComment

One comment of a Reddit thread as returned by GET /v1/reddit/comments/{postId}; the list is flat and in thread order

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Reddit comment ID (without type prefix) |  [optional] |
|**fullname** | **String** | Reddit fullname (e.g. t1_abc123) |  [optional] |
|**parentId** | **String** | Fullname of what the comment answers: the post (t3_…) or a parent comment (t1_…) |  [optional] |
|**author** | **String** | The username, or [deleted] |  [optional] |
|**body** | **String** | Comment text as written (Markdown, not HTML-escaped), or [deleted] / [removed] |  [optional] |
|**permalink** | **String** | Full permalink to the comment |  [optional] |
|**createdUtc** | **BigDecimal** | Unix timestamp of the comment |  [optional] |
|**score** | **Integer** |  |  [optional] |
|**numReplies** | **Integer** | Direct replies included in this response; replies Reddit left out are listed in more |  [optional] |
|**depth** | **Integer** | 0 for a top-level comment of this response, 1 for a reply to it, and so on |  [optional] |
|**isSubmitter** | **Boolean** | Whether the author is the post&#39;s author |  [optional] |
|**edited** | **Boolean** |  |  [optional] |
|**stickied** | **Boolean** |  |  [optional] |
|**distinguished** | **String** | \&quot;moderator\&quot; or \&quot;admin\&quot; when the comment is distinguished, else null |  [optional] |



