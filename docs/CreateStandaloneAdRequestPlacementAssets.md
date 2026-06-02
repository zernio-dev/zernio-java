

# CreateStandaloneAdRequestPlacementAssets

Meta only. Placement asset customization: pin a SPECIFIC image to each placement group on a SINGLE ad (e.g. a 9:16 image on Stories/Reels and a 4:5 on Feed). This is the same thing Meta Ads Manager produces with \"different creative per placement\", mapped to the creative's `asset_feed_spec` + `asset_customization_rules`. It is deterministic pinning, NOT the auto-optimizing pool of `dynamicCreative` (the two are mutually exclusive, and it cannot be combined with `creatives[]` or `adSetId`). The shared copy (headline, body, link, CTA) comes from the top-level single-creative fields (`headline`, `body`, `linkUrl`, `callToAction`) since only the image varies by placement. Each rule's `placements` accepts the same fields as the top-level `placements` object; Meta enforces co-selection rules and returns an actionable error. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultImageUrl** | **URI** | Catch-all image for any placement not matched by a rule. REQUIRED — Meta mandates a default asset customization rule (empty placement spec, lowest priority) on every placement-customized creative.  |  |
|**rules** | [**List&lt;CreateStandaloneAdRequestPlacementAssetsRulesInner&gt;**](CreateStandaloneAdRequestPlacementAssetsRulesInner.md) | One entry per placement group you want to pin a specific image to. |  |



