

# CreateStandaloneAdRequestPlacementAssets

Meta only. Placement asset customization: pin a SPECIFIC asset (image OR video) to each placement group on a SINGLE ad (e.g. a 9:16 on Stories/Reels and a 4:5 on Feed). The same thing Meta Ads Manager produces with \"different creative per placement\", mapped to the creative's `asset_feed_spec` + `asset_customization_rules`. Deterministic pinning, NOT the auto-optimizing pool of `dynamicCreative` (mutually exclusive). Works on the legacy single shape AND the attach shape (`adSetId` + placementAssets adds one placement-customized ad to an existing ad set — the way to build N per-placement ads sharing one ad set: create the first normally, attach the rest). Cannot be combined with `creatives[]`. Shared copy (headline, body, link, CTA) comes from the top-level single-creative fields since only the asset varies by placement. Each rule's `placements` accepts the same fields as the top-level `placements` object; Meta enforces co-selection rules and returns an actionable error.  Note on text rendering: Meta suppresses primary text and headline on fullscreen placements (Stories and Reels) in actual ad delivery; the fields are accepted and the ad publishes, but the copy is not shown to users. For visible copy on those placements, bake the text into the creative image or video itself.  A block is all-image OR all-video, never mixed (Meta's asset_feed_spec carries one ad format). Image mode: `defaultImageUrl` + `rules[].imageUrl`. Video mode: `defaultVideoUrl` + `rules[].videoUrl` (optional `thumbnailUrl`/`defaultThumbnailUrl` posters; Meta auto-generates when omitted). Exactly one catch-all default is required. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultImageUrl** | **URI** | Image mode. Catch-all image for any placement no rule matches. Required in image mode (Meta mandates a default rule). |  [optional] |
|**defaultVideoUrl** | **URI** | Video mode. Catch-all video for any placement no rule matches. Required in video mode. |  [optional] |
|**defaultThumbnailUrl** | **URI** | Video mode (optional). Poster image for the default video; Meta auto-generates one when omitted. |  [optional] |
|**rules** | [**List&lt;CreateStandaloneAdRequestPlacementAssetsRulesInner&gt;**](CreateStandaloneAdRequestPlacementAssetsRulesInner.md) | One entry per placement group you want to pin a specific asset to. |  |



