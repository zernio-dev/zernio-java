

# UpdateAdRequestCreative

Replace the ad's creative. Meta, TikTok, and LinkedIn.  - **Meta**: requires `headline`, `body`, `callToAction`, `linkUrl`, `imageUrl`. The   ad's existing creative is replaced via a new `/act_X/adcreatives` upload + ad   update. The old creative is retained on the ad account for historical reporting. - **TikTok**: patch-style. Pass any subset; `headline` is ignored (TikTok creatives   have no headline slot). `body` becomes the in-feed `ad_text`; `linkUrl` becomes   `landing_page_url`; `videoUrl` triggers a fresh upload. - **LinkedIn**: uploads new media (image via `imageUrl` or video via `videoUrl`),   creates a new inline media creative on the same campaign, and pauses the old   creative (best-effort). The old creative is retained for historical reporting. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headline** | **String** | Meta only |  [optional] |
|**body** | **String** |  |  [optional] |
|**callToAction** | **String** |  |  [optional] |
|**linkUrl** | **URI** |  |  [optional] |
|**imageUrl** | **URI** |  |  [optional] |
|**videoUrl** | **URI** |  |  [optional] |



