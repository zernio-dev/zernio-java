

# UpdateAdRequestCreative

Replace or patch the ad's creative. Meta, TikTok, and LinkedIn.  - **Meta**: patch-style. Pass any subset — fields you omit are preserved from the   live creative, including media (`image_hash`/`video_id` are reused, no re-upload)   and `url_tags`. Sending the full set (`headline`, `body`, `callToAction`,   `linkUrl`, `imageUrl`) rebuilds the creative from scratch instead. Partial   patching reads the live `object_story_spec`, which Meta strips on SHARE /   page-post / dark / asset_feed creatives — those return 422 asking for the full   set. A `videoUrl`/`videoId` on an image creative is a type change and also   needs the full set. `existingCreativeId` repoints the ad at a creative from   GET /v1/ads/creatives and ignores every other field. Meta creatives are   immutable, so any change creates a new creative and repoints the ad; the old   creative is retained on the ad account for historical reporting. - **TikTok**: patch-style. Pass any subset; `headline` is ignored (TikTok creatives   have no headline slot). `body` becomes the in-feed `ad_text`; `linkUrl` becomes   `landing_page_url`; `videoUrl` triggers a fresh upload. `description`, `videoId`   and `existingCreativeId` are Meta-only and return 400. - **LinkedIn**: requires new media (image via `imageUrl` or video via `videoUrl`);   a text-only creative update returns 400. Uploads the media, creates a new inline   media creative on the same campaign, and pauses the old creative (best-effort).   The old creative is retained for historical reporting. `videoId` and   `existingCreativeId` are Meta-only and return 400. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headline** | **String** | Meta and LinkedIn (TikTok has no headline slot) |  [optional] |
|**body** | **String** |  |  [optional] |
|**description** | **String** | Link description slot (Meta &#x60;link_data.description&#x60; / &#x60;video_data.link_description&#x60;, LinkedIn creative description). |  [optional] |
|**callToAction** | **String** |  |  [optional] |
|**linkUrl** | **URI** |  |  [optional] |
|**imageUrl** | **URI** |  |  [optional] |
|**videoUrl** | **URI** |  |  [optional] |
|**videoId** | **String** | Meta only. Reuse an already-uploaded ad video (from POST /v1/ads/videos or GET /v1/ads/videos) instead of re-uploading via videoUrl. |  [optional] |
|**existingCreativeId** | **String** | Meta only. Repoint the ad at an existing library creative (from GET /v1/ads/creatives); all other creative fields are ignored. |  [optional] |



