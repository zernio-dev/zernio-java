

# RedditPlatformData

Posts are either link (with URL/media), native video (via nativeVideo), or self (text-only). Use forceSelf to override. Subreddit defaults to the account's configured one. Some subreddits require a flair.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**subreddit** | **String** | Target subreddit name (without \&quot;r/\&quot; prefix). Overrides the default. Use GET /v1/accounts/{id}/reddit-subreddits to list options. |  [optional] |
|**title** | **String** | Post title. Defaults to the first line of content, truncated to 300 characters. |  [optional] |
|**url** | **URI** | URL for link posts. If provided (and forceSelf is not true), creates a link post instead of a text post. |  [optional] |
|**forceSelf** | **Boolean** | When true, creates a text-only self post and skips native media uploads, even when media is provided. For native video with body text, omit forceSelf and supply content plus a video mediaItem. |  [optional] |
|**flairId** | **String** | Flair ID for the post. Required by some subreddits. Use GET /v1/accounts/{id}/reddit-flairs?subreddit&#x3D;name to list flairs. |  [optional] |
|**flairText** | **String** | Custom flair text, for subreddits that allow free-text flair. Ignored when flairId is provided (flairId wins). |  [optional] |
|**nsfw** | **Boolean** | Mark the post as NSFW (Not Safe For Work / over 18). |  [optional] |
|**spoiler** | **Boolean** | Mark the post as a spoiler. The subreddit must have spoiler tagging enabled for this to take effect. |  [optional] |
|**sendreplies** | **Boolean** | Whether to receive inbox replies for comments on this post. Set to false to opt out. |  [optional] |
|**nativeVideo** | **Boolean** | Controls Reddit&#39;s native video upload flow. When true (default for video mediaItems), the video is uploaded to Reddit&#39;s CDN and submitted with kind&#x3D;video so it renders as an embedded Reddit video player. Reddit transcodes server-side (1080p/30fps cap). Set to false to explicitly publish an external link instead. The post content (or Reddit customContent override) is included as Markdown body text on the native video. When body text is present, upload failures or subreddit video restrictions fail the post without falling back to a link. Automatic link fallback applies only without body text.  |  [optional] |
|**videogif** | **Boolean** | When true (and nativeVideo is active), submits the video as a silent videogif (kind&#x3D;videogif). Use for short looping clips without audio. |  [optional] |
|**videoPosterUrl** | **URI** | Optional poster/thumbnail image URL for native video posts. If omitted, the first frame of the video is extracted and used automatically. |  [optional] |



