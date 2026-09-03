

# TwitterPlatformData

X-specific post options. The article field creates a long-form X Article and is mutually exclusive with tweet media and tweet-only options. Geo-restriction applies at the media level: media is hidden outside the specified countries while tweet text remains visible. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**article** | [**XArticle**](XArticle.md) |  |  [optional] |
|**replyToTweetId** | **String** | ID of an existing tweet to reply to. The published tweet will appear as a reply in that tweet&#39;s thread. For threads, only the first tweet replies to the target; subsequent tweets chain normally. X only permits replying to your own posts or posts you are mentioned in; replying to an arbitrary other account&#39;s post is rejected by X. |  [optional] |
|**quoteTweetId** | **String** | ID (or full status URL) of an existing tweet to quote-repost. The published tweet becomes a quote tweet of the target. Mutually exclusive with media and poll. X only permits quoting your own posts or posts you are mentioned in / part of the conversation thread of; quoting an arbitrary other account&#39;s post is rejected by X. Billed at the standard create rate ($0.015), unlike pasting a tweet URL into the text which is billed at the URL rate ($0.20). For threads, applies to the first tweet only. |  [optional] |
|**replySettings** | [**ReplySettingsEnum**](#ReplySettingsEnum) | Controls who can reply to the tweet. \&quot;following\&quot; allows only people you follow, \&quot;mentionedUsers\&quot; allows only mentioned users, \&quot;subscribers\&quot; allows only subscribers, \&quot;verified\&quot; allows only verified users. Omit for default (everyone can reply). For threads, applies to the first tweet only. Cannot be combined with replyToTweetId. |  [optional] |
|**threadItems** | [**List&lt;TwitterPlatformDataThreadItemsInner&gt;**](TwitterPlatformDataThreadItemsInner.md) | Complete sequence of tweets in a thread. The first item becomes the root tweet, subsequent items are chained as replies. When threadItems is provided, the top-level content field is used only for display and search purposes, it is NOT published. You must include your first tweet as threadItems[0].  |  [optional] |
|**poll** | [**TwitterPlatformDataPoll**](TwitterPlatformDataPoll.md) |  |  [optional] |
|**longVideo** | **Boolean** | Uploads the video with X&#39;s amplify_video media category instead of the standard tweet_video. Applied only when the connected X account has a paid X subscription; on other accounts the flag is accepted and ignored. It is not required to post long videos. The standard tweet_video path already publishes videos well past 140 seconds on free accounts, and maximum duration is set by X per account, not by Zernio. Zernio enforces only the 512 MB file-size limit. Some accounts additionally require X&#39;s long-video API allowlisting, without which X rejects an amplify_video upload. |  [optional] |
|**geoRestriction** | [**GeoRestriction**](GeoRestriction.md) |  |  [optional] |
|**paidPartnership** | **Boolean** | When true, the post is labeled by X as a paid partnership / paid promotion. For threads, applies to the root tweet only. Field availability may depend on your X API access tier. |  [optional] |
|**madeWithAi** | **Boolean** | When true, the post is labeled by X as containing AI-generated media. Per X, this label is for AI-generated media, not AI-written text. For threads, applies to the root tweet only. |  [optional] |
|**sensitiveMedia** | [**TwitterPlatformDataSensitiveMedia**](TwitterPlatformDataSensitiveMedia.md) |  |  [optional] |



## Enum: ReplySettingsEnum

| Name | Value |
|---- | -----|
| FOLLOWING | &quot;following&quot; |
| MENTIONED_USERS | &quot;mentionedUsers&quot; |
| SUBSCRIBERS | &quot;subscribers&quot; |
| VERIFIED | &quot;verified&quot; |



