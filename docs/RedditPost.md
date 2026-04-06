

# RedditPost

A normalized Reddit post returned by the feed and search endpoints

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Reddit post ID (without type prefix) |  [optional] |
|**fullname** | **String** | Reddit fullname (e.g. t3_abc123) |  [optional] |
|**title** | **String** |  |  [optional] |
|**author** | **String** |  |  [optional] |
|**subreddit** | **String** |  |  [optional] |
|**url** | **String** | Post URL (may be a gallery URL |  [optional] |
|**permalink** | **String** | Full permalink to the Reddit post |  [optional] |
|**selftext** | **String** | Self-post body text (empty string for link posts) |  [optional] |
|**createdUtc** | **BigDecimal** | Unix timestamp of post creation |  [optional] |
|**score** | **Integer** |  |  [optional] |
|**numComments** | **Integer** |  |  [optional] |
|**over18** | **Boolean** | Whether the post is marked NSFW |  [optional] |
|**stickied** | **Boolean** |  |  [optional] |
|**flairText** | **String** | Link flair text if set |  [optional] |
|**isGallery** | **Boolean** | Whether the post is a gallery with multiple images |  [optional] |
|**galleryImages** | **List&lt;URI&gt;** | Individual image URLs for gallery posts (only present when isGallery is true) |  [optional] |



