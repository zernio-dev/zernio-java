

# GetInboxPostComments200ResponseCommentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**createdTime** | **OffsetDateTime** |  |  [optional] |
|**from** | [**GetInboxPostComments200ResponseCommentsInnerFrom**](GetInboxPostComments200ResponseCommentsInnerFrom.md) |  |  [optional] |
|**likeCount** | **Integer** |  |  [optional] |
|**replyCount** | **Integer** | The platform&#39;s own reply count, which includes hidden and deleted replies. Can exceed replies[].length even when repliesHasMore is false or absent. |  [optional] |
|**platform** | **String** | The platform this comment is from |  [optional] |
|**url** | **String** | Direct link to the comment on the platform (if available) |  [optional] |
|**replies** | **List&lt;Object&gt;** |  |  [optional] |
|**repliesHasMore** | **Boolean** | Facebook only. True when replies[] (capped at 10) does not hold the comment&#39;s full reply thread.  Fetch the rest by passing the comment id as the &#x60;commentId&#x60; query parameter to GET /v1/inbox/comments/{postId} (or, for backwards compatibility, as &#x60;postId&#x60;).  Absent (not false) on every other platform, including Instagram, which has no equivalent signal.  |  [optional] |
|**canReply** | **Boolean** | Whether this comment can be replied to. Always present. |  [optional] |
|**canDelete** | **Boolean** | Whether DELETE is expected to work on this comment. True for the account&#39;s own comments, and for anyone&#39;s comment on Facebook, Instagram, YouTube and LinkedIn organization accounts. On TikTok, TikTok&#39;s own flag decides. False does not block the call: the platform decides. Always present. |  [optional] |
|**canHide** | **Boolean** | Whether hide is supported for this comment&#39;s platform (Facebook, Instagram, Threads, X, TikTok). It does not check each comment: X needs a conversation started by the account, and Threads only hides top-level replies. Always present. |  [optional] |
|**canLike** | **Boolean** | Whether this comment can be liked (Facebook, X, Bluesky, Reddit, LinkedIn, TikTok). Always present. |  [optional] |
|**isHidden** | **Boolean** | Whether the comment is currently hidden. On Instagram accounts connected through Facebook Login, Meta leaves hidden comments (and their replies) out of the list entirely, so they never appear with isHidden true; Instagram Login accounts and Facebook Pages return them with isHidden true. |  [optional] |
|**isLiked** | **Boolean** | Whether the current user has liked this comment |  [optional] |
|**attachment** | [**CommentAttachment**](CommentAttachment.md) | The comment&#39;s media, whenever the platform returns one (replies included). Supported on Facebook, TikTok, X, Threads and Bluesky; absent when the comment has no media and on every other platform. See CommentAttachment for each platform&#39;s &#x60;type&#x60; values. |  [optional] |
|**likeUri** | **String** | Bluesky like URI for unliking |  [optional] |
|**cid** | **String** | Bluesky content identifier |  [optional] |
|**parentId** | **String** | ID of the parent comment.  - Facebook and Instagram: present on entries inside replies[]; omitted on top-level entries. - X: present inside replies[] and on top-level entries, where it holds the ID of the post replied to. - Every other platform: omitted; the parent relationship is expressed only through replies[] nesting.  When omitted, the key is absent, not null. |  [optional] |
|**rootUri** | **String** | Bluesky root post URI |  [optional] |
|**rootCid** | **String** | Bluesky root post CID |  [optional] |



