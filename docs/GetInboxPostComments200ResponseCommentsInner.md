

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
|**repliesHasMore** | **Boolean** | Facebook only. True when replies[] (capped at 10) does not hold the comment&#39;s full reply thread; fetch the rest by passing the comment id as the &#x60;commentId&#x60; query parameter to GET /v1/inbox/comments/{postId} (or, for backwards compatibility, as &#x60;postId&#x60;). Absent (not false) on every other platform, including Instagram, which has no equivalent signal. |  [optional] |
|**canReply** | **Boolean** |  |  [optional] |
|**canDelete** | **Boolean** |  |  [optional] |
|**canHide** | **Boolean** | Whether this comment can be hidden (Facebook, Instagram, Threads) |  [optional] |
|**canLike** | **Boolean** | Whether this comment can be liked (Facebook, X, Bluesky, Reddit, LinkedIn) |  [optional] |
|**isHidden** | **Boolean** | Whether the comment is currently hidden. On Instagram accounts connected through Facebook Login, Meta leaves hidden comments (and their replies) out of the list entirely, so they never appear with isHidden true; Instagram Login accounts and Facebook Pages return them with isHidden true. |  [optional] |
|**isLiked** | **Boolean** | Whether the current user has liked this comment |  [optional] |
|**likeUri** | **String** | Bluesky like URI for unliking |  [optional] |
|**cid** | **String** | Bluesky content identifier |  [optional] |
|**parentId** | **String** | ID of the parent comment. Present on entries inside replies[] for Facebook, Instagram and X. On X it is also present on top-level entries, where it holds the ID of the post replied to. Omitted entirely (key absent, not null) on top-level Facebook and Instagram entries and on every other platform, which express the parent relationship only through replies[] nesting. |  [optional] |
|**rootUri** | **String** | Bluesky root post URI |  [optional] |
|**rootCid** | **String** | Bluesky root post CID |  [optional] |



