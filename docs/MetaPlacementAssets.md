

# MetaPlacementAssets

Meta placement asset customization: pin a SPECIFIC asset (image OR video) to each placement group on a SINGLE ad (e.g. a 4:5 image on Feed and a 9:16 image on Stories/Reels), the same thing Meta Ads Manager produces with \"different creative per placement\". Mapped to the creative's `asset_feed_spec` (`optimization_type: PLACEMENT`) + `asset_customization_rules`. Each rule can pin one `headline`, `body` and `description`; omitted fields and unmatched placements use the request's top-level copy. Each rule's `placements` accepts the same fields as the top-level `placements` object; Meta enforces co-selection rules and returns an actionable error.  A block is all-image OR all-video, never mixed (Meta's asset_feed_spec carries one ad format). Image mode: `defaultImageUrl` + `rules[].imageUrl`. Video mode: `defaultVideoUrl` + `rules[].videoUrl` (optional `thumbnailUrl`/`defaultThumbnailUrl` posters; Meta auto-generates when omitted). Exactly one catch-all default is required.  Meta controls text rendering by placement and format. Validation accepts these fields but does not prove that every field appears in delivery. Preview the ad; put copy that must always be visible into the image or video itself. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultImageUrl** | **URI** | Image mode. Catch-all image for any placement no rule matches. Required in image mode (Meta mandates a default rule). |  [optional] |
|**defaultVideoUrl** | **URI** | Video mode. Catch-all video for any placement no rule matches. Required in video mode. |  [optional] |
|**defaultThumbnailUrl** | **URI** | Video mode (optional). Poster image for the default video; Meta auto-generates one when omitted. |  [optional] |
|**rules** | [**List&lt;MetaPlacementAssetsRulesInner&gt;**](MetaPlacementAssetsRulesInner.md) | One entry per placement group you want to pin a specific asset to. |  |



