

# AccountWithFollowerStatsAllOfAccountStats

Platform-specific account counters from the latest daily snapshot. Each platform reports its own subset of the keys below, and no other key is returned. Absent when the platform reports none of them. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**followingCount** | **BigDecimal** | Number of accounts being followed (TikTok, X, Pinterest, Bluesky) |  [optional] |
|**followsCount** | **BigDecimal** | Number of accounts being followed (Instagram) |  [optional] |
|**mediaCount** | **BigDecimal** | Total media posts (Instagram) |  [optional] |
|**videoCount** | **BigDecimal** | Total videos (YouTube, TikTok) |  [optional] |
|**tweetCount** | **BigDecimal** | Total tweets (X) |  [optional] |
|**postsCount** | **BigDecimal** | Total posts (Bluesky) |  [optional] |
|**pinCount** | **BigDecimal** | Total pins (Pinterest) |  [optional] |
|**totalViews** | **BigDecimal** | Total channel views (YouTube) |  [optional] |
|**likesCount** | **BigDecimal** | Total likes received (TikTok) |  [optional] |
|**monthlyViews** | **BigDecimal** | Monthly profile views (Pinterest). null when Pinterest reports no window |  [optional] |
|**listedCount** | **BigDecimal** | Lists the user appears on (X) |  [optional] |
|**boardCount** | **BigDecimal** | Total boards (Pinterest) |  [optional] |



