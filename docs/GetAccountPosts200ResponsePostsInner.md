

# GetAccountPosts200ResponsePostsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The platform&#39;s own post id (the video ID on YouTube) |  [optional] |
|**platform** | **String** |  |  [optional] |
|**message** | **String** | Caption or title, empty string when the post has no text |  [optional] |
|**createdTime** | **OffsetDateTime** |  |  [optional] |
|**permalink** | **String** | Public URL of the post on the platform |  [optional] |
|**picture** | **String** | Thumbnail or media URL |  [optional] |
|**mediaType** | **String** |  |  [optional] |
|**commentCount** | **Integer** |  |  [optional] |
|**likeCount** | **Integer** |  |  [optional] |
|**reactionCount** | **Integer** | Facebook and LinkedIn only |  [optional] |
|**shareCount** | **Integer** |  |  [optional] |
|**cid** | **String** | Bluesky content id, required to reply to the post |  [optional] |
|**subreddit** | **String** | Reddit only |  [optional] |
|**title** | **String** | Pinterest only: native Pin title |  [optional] |
|**description** | **String** | Pinterest only: full native Pin description (Pinterest caps it at 800 characters) |  [optional] |
|**link** | **String** | Pinterest only: destination URL of the Pin, not the Pin page (see permalink) |  [optional] |
|**boardId** | **String** | Pinterest only: id of the board holding the Pin |  [optional] |
|**boardOwnerUsername** | **String** | Pinterest only: username of the board owner |  [optional] |



