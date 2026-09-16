

# GetPostTimeline200ResponseTimelineInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **LocalDate** | Date in YYYY-MM-DD format |  [optional] |
|**platform** | **String** | Platform name (e.g. instagram, tiktok) |  [optional] |
|**platformPostId** | **String** | Platform-specific post ID |  [optional] |
|**impressions** | **Integer** | Total impressions on this date |  [optional] |
|**reach** | **Integer** | Total reach on this date |  [optional] |
|**likes** | **Integer** | Total likes on this date |  [optional] |
|**comments** | **Integer** | Total comments on this date |  [optional] |
|**shares** | **Integer** | Total shares on this date |  [optional] |
|**saves** | **Integer** | Total saves on this date |  [optional] |
|**clicks** | **Integer** | Total clicks on this date |  [optional] |
|**views** | **Integer** | Total views on this date |  [optional] |
|**follows** | **Integer** | Follows attributed to the post on this date (Instagram feed and stories, TikTok business lane); 0 elsewhere |  [optional] |
|**completionRate** | **BigDecimal** | TikTok business lane: share of viewers who watched to the end on this date, 0 to 1; 0 elsewhere |  [optional] |
|**profileViews** | **Integer** | TikTok business lane: profile views attributed to the post on this date; 0 elsewhere |  [optional] |
|**websiteClicks** | **Integer** | TikTok business lane: website-link clicks attributed to the post on this date (also inside clicks); 0 elsewhere |  [optional] |
|**impressionSources** | **Map&lt;String, BigDecimal&gt;** | TikTok business lane: share of views by surface on this date (forYou, follow, search, personalProfile, sound, directMessage, other), fractions 0 to 1; empty object elsewhere |  [optional] |
|**audienceTypes** | **Map&lt;String, BigDecimal&gt;** | TikTok business lane: follower / nonFollower and newViewer / returnViewer shares on this date, fractions 0 to 1; empty object elsewhere |  [optional] |



