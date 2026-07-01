

# ExternalPostSummaryAnalytics

Engagement + insights for the post. `likes` and `comments` are available immediately after an on-demand sync (they come from the platform listing). `reach`, `impressions`, `views` depend on the platform's insights, which carry their own delay (e.g. ~24h on Instagram) and read 0 until the platform makes them available. 

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
|**engagementRate** | **BigDecimal** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** | When these metrics were last refreshed |  [optional] |



