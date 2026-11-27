

# ExternalPostSummaryAnalytics

Not a source of metrics: read a post's metrics from GET /v1/analytics.  - A post read from Zernio's records (the recent posts list, or a   matched post that was already stored): usually `null` or only   `lastUpdated`. - Archived Instagram stories and posts first synced before metrics   moved to GET /v1/analytics: metric fields that are final or no   longer refreshed. Do not use them. - A post imported by this call (a LinkedIn personal profile post, a   TikTok Business post or a Pinterest Pin fetched by `url`/`postId`):   the values just fetched. A LinkedIn re-import of the same post   within about 15 seconds returns the stored record without metrics. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**likes** | **Integer** |  |  [optional] |
|**comments** | **Integer** |  |  [optional] |
|**shares** | **Integer** |  |  [optional] |
|**saves** | **Integer** |  |  [optional] |
|**sends** | **Integer** |  |  [optional] |
|**clicks** | **Integer** |  |  [optional] |
|**views** | **Integer** |  |  [optional] |
|**reach** | **Integer** |  |  [optional] |
|**impressions** | **Integer** |  |  [optional] |
|**engagementRate** | **BigDecimal** | Percentage, rounded to 2 decimals. Same definition as PostAnalytics.engagementRate: (likes + comments + shares + saves) / (impressions or reach or views) * 100, where the denominator is the first of the three that is non-zero. Clicks and follows are never counted. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | When these metrics were last refreshed |  [optional] |



