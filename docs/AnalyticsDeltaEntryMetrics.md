

# AnalyticsDeltaEntryMetrics

Metrics a platform does not report are 0, not absent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**impressions** | **Integer** |  |  |
|**reach** | **Integer** |  |  |
|**likes** | **Integer** |  |  |
|**comments** | **Integer** |  |  |
|**shares** | **Integer** |  |  |
|**saves** | **Integer** |  |  |
|**sends** | **Integer** |  |  |
|**clicks** | **Integer** |  |  |
|**views** | **Integer** |  |  |
|**follows** | **Integer** | Follows attributed to this post (Instagram feed and stories, Facebook Reels, TikTok business lane) |  |
|**igReelsAvgWatchTime** | **Integer** | Average watch time per play, in milliseconds (Instagram Reels, Facebook Reels, TikTok business videos) |  |
|**igReelsVideoViewTotalTime** | **Integer** | Total watch time including replays, in milliseconds (Instagram Reels, Facebook Reels, TikTok business videos) |  |
|**reposts** | **Integer** |  |  |
|**reelsSkipRate** | **BigDecimal** | Instagram Reels skip rate, 0 to 1 |  |
|**completionRate** | **BigDecimal** | TikTok business lane: share of viewers who watched to the end, 0 to 1 |  |
|**profileViews** | **Integer** | TikTok business lane: profile views attributed to the post |  |
|**websiteClicks** | **Integer** | TikTok business lane: website-link clicks attributed to the post (also inside clicks) |  |
|**impressionSources** | **Map&lt;String, BigDecimal&gt;** | TikTok business lane: share of views by surface (forYou, follow, search, personalProfile, sound, directMessage, other), fractions 0 to 1. Empty object elsewhere. |  |
|**audienceTypes** | **Map&lt;String, BigDecimal&gt;** | TikTok business lane: follower / nonFollower and newViewer / returnViewer shares, fractions 0 to 1. Empty object elsewhere. |  |
|**audienceCountries** | **Map&lt;String, BigDecimal&gt;** | TikTok business lane: viewer-country shares keyed by ISO-3166 alpha-2, fractions 0 to 1, top 20 with the tail in &#x60;other&#x60;. Empty object elsewhere. |  |
|**replays** | **Integer** | Facebook Reels only: plays that were replays. 0 elsewhere. |  [optional] |
|**retentionCurve** | **Map&lt;String, BigDecimal&gt;** | Facebook Reels only: share of plays still watching at each second of playback, fractions 0 to 1 (Meta post_video_retention_graph). Keys are whole seconds from the start of a play (\&quot;3\&quot; is the share still watching at 3 s). Loops count as continued playback, so a short Reels curve runs past its length (an 8 s Reel has keys \&quot;0\&quot; to \&quot;12\&quot;); Meta returns at most 41 points, so a long Reel covers only its first 40 s. Empty object elsewhere. |  [optional] |



