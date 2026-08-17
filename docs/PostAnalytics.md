

# PostAnalytics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**impressions** | **Integer** |  |  [optional] |
|**reach** | **Integer** |  |  [optional] |
|**likes** | **Integer** |  |  [optional] |
|**comments** | **Integer** |  |  [optional] |
|**shares** | **Integer** |  |  [optional] |
|**saves** | **Integer** | Number of saves/bookmarks (Instagram, Pinterest, X/Twitter) |  [optional] |
|**clicks** | **Integer** |  |  [optional] |
|**views** | **Integer** |  |  [optional] |
|**follows** | **Integer** | Instagram feed posts and stories only: organic accounts that started following from this post. 0 for reels and other platforms. |  [optional] |
|**igReelsAvgWatchTime** | **Integer** | Instagram Reels only: average watch time per play, in milliseconds. 0 for non-Reels media and other platforms. |  [optional] |
|**igReelsVideoViewTotalTime** | **Integer** | Instagram Reels only: total watch time including replays, in milliseconds. 0 for non-Reels media and other platforms. |  [optional] |
|**videoDurationSeconds** | **Integer** | Video length in seconds. Currently Instagram Reels only; combine with igReelsAvgWatchTime (ms) to estimate retention. Null when unknown (other platforms, non-video media, or when Instagram does not expose the media URL, e.g. reels with copyrighted audio). |  [optional] |
|**engagementRate** | **BigDecimal** | Percentage, rounded to 2 decimals: (likes + comments + shares + saves) / (impressions or reach or views) * 100. Clicks and follows are never counted. The denominator is the FIRST of impressions, reach, views that is non-zero, so it is not the same basis on every post: a post with impressions divides by impressions, one without falls back to reach, then to views. If you need a single consistent basis (e.g. interactions / reach), compute it from the raw fields above. The engagementRate on the LinkedIn account endpoints is a different formula. |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |



