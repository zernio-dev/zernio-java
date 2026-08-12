

# AdEngagementCounts

The single `engagement` total split into the interactions behind it.  Note that `engagement` is not the sum of these: Meta's own `post_engagement` and `page_engagement` totals already contain the individual interactions, and all of them are counted into `engagement`. Use these fields when you need a specific interaction, and `engagement` only as the coarse total it has always been.  Populated for Meta and, since 2026-08, TikTok (`reactions` = paid likes, `comments`, `shares`; TikTok's `follow` count lives in `actions.follow`, not here). Other platforms leave these at 0. TikTok history note: paused TikTok ads are not re-synced, so campaigns that ended before the rollout keep 0s here. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postEngagement** | **Integer** | Meta&#39;s own post-engagement total (&#x60;post_engagement&#x60;). Meta-only. |  [optional] |
|**pageEngagement** | **Integer** | Meta&#39;s own page-engagement total (&#x60;page_engagement&#x60;). Meta-only. |  [optional] |
|**reactions** | **Integer** | Reactions on the ad&#39;s post (&#x60;post_reaction&#x60;). For TikTok these are its paid likes. |  [optional] |
|**comments** | **Integer** | Comments on the ad&#39;s post. |  [optional] |
|**shares** | **Integer** | Shares of the ad&#39;s post. Meta reports these under the action type literally named &#x60;post&#x60;; TikTok under &#x60;share&#x60;. |  [optional] |
|**saves** | **Integer** | Saves of the ad&#39;s post (&#x60;onsite_conversion.post_save&#x60;). |  [optional] |
|**pageLikes** | **Integer** | New Page likes attributed to the ad (&#x60;like&#x60;). |  [optional] |
|**videoViews** | **Integer** | 3-second video views (&#x60;video_view&#x60;). For completion-based counts use &#x60;videoThruplayWatchedActions&#x60;. |  [optional] |
|**linkClicks** | **Integer** | Attributed link clicks (&#x60;link_click&#x60;). This is the attribution-window count, which differs from the in-session count in the sibling &#x60;inlineLinkClicks&#x60; field. |  [optional] |



