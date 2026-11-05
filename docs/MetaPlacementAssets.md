

# MetaPlacementAssets

Meta placement asset customization: pin a SPECIFIC asset (image OR video) to each placement group on a SINGLE ad (e.g. a 4:5 image on Feed and a 9:16 image on Stories/Reels). This is what Meta Ads Manager produces with \"different creative per placement\".  Mapped to the creative's `asset_feed_spec` (`optimization_type: PLACEMENT`) + `asset_customization_rules`.  - Each rule can pin one `headline`, `body` and `description`; omitted fields and unmatched placements use the request's top-level copy. - Each rule's `placements` accepts the same fields as the top-level `placements` object. Meta enforces co-selection rules and returns an actionable error.  A block is all-image OR all-video, never mixed (Meta's asset_feed_spec carries one ad format). Exactly one catch-all default is required.  - Image mode: `defaultImageUrl` + `rules[].imageUrl`. - Video mode: `defaultVideoUrl` or `defaultVideoId` + `rules[].videoUrl` or `rules[].videoId`, with optional `thumbnailUrl`/`defaultThumbnailUrl` posters (Meta auto-generates them when omitted). An id reuses a video already on the ad account and wins over a URL in the same slot; the two can mix across slots.  Meta controls text rendering by placement and format. Validation accepts these fields but does not prove every field appears in delivery. Preview the ad, and put copy that must always be visible into the image or video itself. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultImageUrl** | **URI** | Image mode. Catch-all image for any placement no rule matches. Required in image mode (Meta mandates a default rule). |  [optional] |
|**defaultVideoUrl** | **URI** | Video mode. Catch-all video for any placement no rule matches. Video mode requires this or &#x60;defaultVideoId&#x60;. |  [optional] |
|**defaultVideoId** | **String** | Video mode. ID of a video already on the ad account, used as the catch-all instead of uploading &#x60;defaultVideoUrl&#x60;. Wins over &#x60;defaultVideoUrl&#x60;. A video still processing after 30 seconds returns 409. |  [optional] |
|**defaultThumbnailUrl** | **URI** | Video mode (optional). Poster image for the default video; Meta auto-generates one when omitted. |  [optional] |
|**rules** | [**List&lt;MetaPlacementAssetsRulesInner&gt;**](MetaPlacementAssetsRulesInner.md) | One entry per placement group you want to pin a specific asset to. |  |



