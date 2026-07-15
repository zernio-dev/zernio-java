

# AdDailyMetrics

One day of metrics. Same fields as `AdMetrics` plus the `date` they apply to. Returned inside a node's `daily[]` when `GET /v1/ads/tree` is called with `timeIncrement=1`. Rate metrics (ctr/cpc/cpm/costPerConversion/ roas/videoAvgTimeWatchedActions) are recomputed per day from that day's sums, so summing the additive fields across a node's `daily[]` reproduces its aggregated `metrics` total. Do NOT sum or plain-average `videoAvgTimeWatchedActions` across days: the range value is the play-weighted average of the daily values. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spend** | **BigDecimal** |  |  [optional] |
|**impressions** | **Integer** |  |  [optional] |
|**reach** | **Integer** |  |  [optional] |
|**clicks** | **Integer** |  |  [optional] |
|**ctr** | **BigDecimal** | Click-through rate (%) |  [optional] |
|**cpc** | **BigDecimal** | Cost per click |  [optional] |
|**cpm** | **BigDecimal** | Cost per 1000 impressions |  [optional] |
|**engagement** | **Integer** |  |  [optional] |
|**conversions** | **Integer** | Count of conversion events over the requested date range. Meta: events matching the campaign&#39;s promoted_object.custom_event_type (PURCHASE, LEAD, etc.). Google: the account&#39;s tracked conversions. X and LinkedIn: their reported website/lead conversions (added 2026-07). 0 for non-conversion campaigns or when no events have fired. |  [optional] |
|**costPerConversion** | **BigDecimal** | Derived spend / conversions in the same currency as spend. 0 when conversions is 0. |  [optional] |
|**actions** | **Map&lt;String, Integer&gt;** | Per-action-type counts summed over the date range, keyed by the platform&#39;s action-type names. Meta: raw Insights action_type keys (link_click, offsite_conversion.fb_pixel_purchase, onsite_conversion.lead_grouped, ...) — both engagement and conversion events. X: conversion types (purchase, sign_up, site_visit, download, custom). LinkedIn: conversion types (post_click, post_view, lead_gen). Google returns {} (its per-action names aren&#39;t synced per ad). Empty object when no actions are reported. NOTE: keys differ by platform, so branch on the ad&#39;s platform when interpreting them. |  [optional] |
|**actionValues** | **Map&lt;String, BigDecimal&gt;** | Monetary mirror of &#x60;actions&#x60;, from Meta&#39;s Insights &#x60;action_values[]&#x60; array. Same keying — values are the revenue attributed to each action_type, in ad-account native currency (same unit as &#x60;spend&#x60;; see the campaign node&#39;s &#x60;currency&#x60; field). Use this to compute revenue-per-event (e.g. avg purchase value). Meta-only; other platforms return {}. |  [optional] |
|**purchaseValue** | **BigDecimal** | Convenience sum of purchase-type action values — picked from &#x60;actionValues&#x60; via the same priority list as &#x60;conversions&#x60; so both fields describe the same events. In ad-account native currency. 0 when the campaign has no purchase event configured. Meta-only. |  [optional] |
|**roas** | **BigDecimal** | Return on ad spend — derived as &#x60;purchaseValue / spend&#x60;. 0 when &#x60;spend&#x60; is 0. Equivalent to Meta&#39;s &#x60;purchase_roas&#x60; under default attribution. At ad-set and campaign levels this is recomputed from summed purchaseValue + spend (NOT averaged across children) so it&#39;s mathematically correct at every rollup level. |  [optional] |
|**videoPlayActions** | **Integer** | Meta video ads only (0 for non-video ads and other platforms), like all video* fields below. Number of times the video started playing (Meta &#x60;video_play_actions&#x60;), summed over the date range and across children at ad-set/campaign level. |  [optional] |
|**video30SecWatchedActions** | **Integer** | Views of at least 30 seconds (or to the end, for shorter videos). Meta &#x60;video_30_sec_watched_actions&#x60;. |  [optional] |
|**videoThruplayWatchedActions** | **Integer** | ThruPlays (watched to completion, or at least 15 seconds). Meta &#x60;video_thruplay_watched_actions&#x60;. |  [optional] |
|**videoP25WatchedActions** | **Integer** | Views reaching 25% of the video&#39;s length. With the other percentile fields, powers hook/hold/drop-off analysis (e.g. hook rate &#x3D; videoP25WatchedActions / videoPlayActions). Meta &#x60;video_p25_watched_actions&#x60;. |  [optional] |
|**videoP50WatchedActions** | **Integer** | Views reaching 50% of the video&#39;s length. Meta &#x60;video_p50_watched_actions&#x60;. |  [optional] |
|**videoP75WatchedActions** | **Integer** | Views reaching 75% of the video&#39;s length. Meta &#x60;video_p75_watched_actions&#x60;. |  [optional] |
|**videoP95WatchedActions** | **Integer** | Views reaching 95% of the video&#39;s length. Meta &#x60;video_p95_watched_actions&#x60;. |  [optional] |
|**videoP100WatchedActions** | **Integer** | Views reaching 100% of the video&#39;s length. Meta &#x60;video_p100_watched_actions&#x60;. |  [optional] |
|**videoAvgTimeWatchedActions** | **BigDecimal** | Average seconds watched per play (Meta &#x60;video_avg_time_watched_actions&#x60;). Aggregated over date ranges and across children as a play-weighted average (total watch time / total plays), never a plain average of averages. |  [optional] |
|**lastSyncedAt** | **OffsetDateTime** | Present on individual ads only, not on campaign aggregations |  [optional] |
|**date** | **LocalDate** | Calendar day (YYYY-MM-DD) these metrics apply to. |  [optional] |



