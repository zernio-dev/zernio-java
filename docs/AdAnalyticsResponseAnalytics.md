

# AdAnalyticsResponseAnalytics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**summary** | [**AdMetrics**](AdMetrics.md) |  |  [optional] |
|**daily** | [**List&lt;CampaignAnalyticsResponseAnalyticsDailyInner&gt;**](CampaignAnalyticsResponseAnalyticsDailyInner.md) |  |  [optional] |
|**breakdowns** | **Map&lt;String, List&lt;Object&gt;&gt;** | Requested demographic breakdowns, keyed by dimension. Fetched live from the platform per request and never stored, so these rows can carry fields the stored &#x60;summary&#x60; and &#x60;daily&#x60; series do not.  LinkedIn rows carry &#x60;value&#x60; (the pivot URN), &#x60;name&#x60; (resolved label where LinkedIn provides one), the usual spend/impressions/clicks/ctr/cpc/cpm/engagement figures, plus two reach fields:  - &#x60;reach&#x60;: the segment&#39;s &#x60;approximateMemberReach&#x60;. - &#x60;audiencePenetration&#x60;: LinkedIn&#39;s own ratio of members reached to the size of   the targeted audience, passed through verbatim.  LinkedIn withholds both below its audience privacy threshold, in which case the keys are ABSENT rather than 0. &#x60;audiencePenetration&#x60; is available here only: it is not part of the stored metrics series.  TikTok rows are keyed by TikTok&#39;s own dimension name (&#x60;country_code&#x60; for &#x60;country&#x60;, &#x60;platform&#x60; for &#x60;publisher_platform&#x60;). &#x60;placement&#x60; rows carry the label TikTok Ads Manager shows (&#x60;TikTok&#x60;, &#x60;TikTok Ad Network&#x60;, &#x60;News Feed App Series&#x60;) in &#x60;placement&#x60; and TikTok&#39;s API value (&#x60;PLACEMENT_TIKTOK&#x60;, &#x60;PLACEMENT_PANGLE&#x60;, &#x60;PLACEMENT_GLOBAL_APP_BUNDLE&#x60;) in &#x60;placementRaw&#x60;; a value without a known label carries the raw value in both.  A requested dimension with no data in the range is an empty array.  |  [optional] |
|**unsupportedBreakdowns** | **List&lt;String&gt;** | Requested breakdowns this platform cannot break down by (e.g. region on TikTok, any breakdown on Google). Absent when every requested breakdown is supported. |  [optional] |
|**breakdownHints** | **Map&lt;String, String&gt;** | Guidance for some names in unsupportedBreakdowns, keyed by that name (e.g. placement on Meta points at publisher_platform and platform_position; platform_position on TikTok points at placement). Absent when no unsupported name has a hint. |  [optional] |
|**breakdownErrors** | [**List&lt;CampaignAnalyticsResponseAnalyticsBreakdownErrorsInner&gt;**](CampaignAnalyticsResponseAnalyticsBreakdownErrorsInner.md) | TikTok only: breakdowns the platform failed to return (rate limit, permission, rejected query). Each one is an empty array under breakdowns; summary and daily are unaffected. Absent when every breakdown answered. |  [optional] |
|**breakdownDroppedMetrics** | **Map&lt;String, List&lt;String&gt;&gt;** | TikTok only: TikTok metric names TikTok refused for a breakdown, keyed by the requested breakdown (e.g. total_purchase and total_purchase_value have no relation to platform, ac or language). Every row value derived from a refused metric is null in that breakdown (purchaseValue and roas, or the matching actions and actionValues entries), never a number computed without it. Absent when no metric was refused. |  [optional] |
|**breakdownsRange** | [**CampaignAnalyticsResponseAnalyticsBreakdownsRange**](CampaignAnalyticsResponseAnalyticsBreakdownsRange.md) |  |  [optional] |



