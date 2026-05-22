

# GetInboxPostComments200ResponsePost

(Reddit only) Metadata for the target post, returned alongside the comments in Reddit's single round-trip. Lets integrators render a preview of the post the user is commenting on without an additional request. Absent for non-Reddit platforms and when the upstream response is missing the post listing (deleted post, malformed response). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Reddit post base36 id (e.g. \&quot;1tjtj26\&quot;) |  [optional] |
|**fullname** | **String** | Fullname with type prefix (e.g. \&quot;t3_1tjtj26\&quot;) |  [optional] |
|**title** | **String** |  |  [optional] |
|**selftext** | **String** | Body text for self-posts (empty for link posts) |  [optional] |
|**author** | **String** | Reddit username |  [optional] |
|**subreddit** | **String** | Subreddit name |  [optional] |
|**permalink** | **String** | Absolute URL to the post on reddit.com |  [optional] |
|**url** | **String** | For link posts |  [optional] |
|**score** | **Integer** | Net upvotes (upvotes minus downvotes) |  [optional] |
|**numComments** | **Integer** |  |  [optional] |
|**createdUtc** | **Integer** | Unix timestamp in seconds |  [optional] |
|**over18** | **Boolean** |  |  [optional] |
|**stickied** | **Boolean** |  |  [optional] |
|**flairText** | **String** | Link flair text if any |  [optional] |
|**isGallery** | **Boolean** | True if the post is a Reddit gallery (multiple images) |  [optional] |



