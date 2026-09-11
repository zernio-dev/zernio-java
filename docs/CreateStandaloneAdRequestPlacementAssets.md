

# CreateStandaloneAdRequestPlacementAssets

Meta only. Placement asset customization: pin a SPECIFIC asset (image OR video) to each placement group on a SINGLE ad (e.g. a 9:16 on Stories/Reels and a 4:5 on Feed). The same thing Meta Ads Manager produces with \"different creative per placement\", mapped to the creative's `asset_feed_spec` + `asset_customization_rules`. Deterministic pinning, NOT the auto-optimizing pool of `dynamicCreative` (mutually exclusive). Works on the legacy single shape AND the attach shape (`adSetId` + placementAssets adds one placement-customized ad to an existing ad set, the way to build N per-placement ads sharing one ad set: create the first normally, attach the rest). Cannot be combined with `creatives[]` or top-level `bodies`/`headlines`/`descriptions` arrays. Each rule can override `headline`, `body` and `description` with one string per field. Omitted fields and unmatched placements use the top-level copy; `linkUrl` and `callToAction` remain shared. Zernio emits labelled text with `optimization_type: PLACEMENT`. Multiple text options rotating within a placement are not supported by this input. Each rule's `placements` accepts the same fields as the top-level `placements` object; Meta enforces co-selection rules and returns an actionable error.  Meta controls text rendering by placement and format. Validation accepts these fields but does not prove that every field appears in delivery. Preview the ad; put copy that must always be visible into the image or video itself.  `validateOnly: true` supports all-image placementAssets without uploading or creating anything. Video placement validation remains unsupported because it requires uploads.  A block is all-image OR all-video, never mixed (Meta's asset_feed_spec carries one ad format). Image mode: `defaultImageUrl` + `rules[].imageUrl`. Video mode: `defaultVideoUrl` + `rules[].videoUrl` (optional `thumbnailUrl`/`defaultThumbnailUrl` posters; Meta auto-generates when omitted). Exactly one catch-all default is required. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultImageUrl** | **URI** | Image mode. Catch-all image for any placement no rule matches. Required in image mode (Meta mandates a default rule). |  [optional] |
|**defaultVideoUrl** | **URI** | Video mode. Catch-all video for any placement no rule matches. Required in video mode. |  [optional] |
|**defaultThumbnailUrl** | **URI** | Video mode (optional). Poster image for the default video; Meta auto-generates one when omitted. |  [optional] |
|**rules** | [**List&lt;CreateStandaloneAdRequestPlacementAssetsRulesInner&gt;**](CreateStandaloneAdRequestPlacementAssetsRulesInner.md) | One entry per placement group you want to pin a specific asset to. |  |



