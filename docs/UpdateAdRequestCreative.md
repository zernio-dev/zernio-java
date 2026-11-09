

# UpdateAdRequestCreative

Replace or patch the ad's creative. Meta, TikTok, and LinkedIn.  **Meta**: patch-style.  - Pass any subset: omitted fields are preserved from the live creative, including media (`image_hash`/`video_id` reused, no re-upload) and `url_tags`. Sending the full set (`headline`, `body`, `callToAction`, `linkUrl`, `imageUrl`) rebuilds the creative from scratch. - Partial patching reads the live `object_story_spec`, which Meta strips on SHARE / page-post / dark post creatives; those return 422 asking for the full set. A `videoUrl`/`videoId` on an image creative is a type change and also needs the full set. - Creatives with an `asset_feed_spec` (several text options, placement or language rules) take text, link, tracking and enhancement edits in place. The new creative is built from the live asset feed with the edited text, and every video, image, label and rule is kept. - On those, `body`, `headline` and `description` replace the one option of that kind. When the feed has several, send `bodies`, `headlines` or `descriptions` with one text per option, in order. `linkUrl` replaces the feed's only destination link. - Image, video and call-to-action changes on asset_feed creatives apply to the story spec (Multiple Text Options creatives). They return 422 when the feed itself holds the images, videos or call-to-action options. - The live creative's deprecated `standard_enhancements` setting (Meta subcode 3858504) is never sent back; every other enhancement setting is kept. - `existingCreativeId` repoints the ad at a creative from GET /v1/ads/creatives and ignores every other field. - Meta creatives are immutable: any change creates a new creative and repoints the ad. The old creative stays on the ad account for historical reporting. - `creativeFeatures` is Meta-only. Omitted settings are preserved from the live creative, including on full rebuilds; a supplied creativeFeatures map overrides individual existing keys.  - A `creative` object with no recognised field (`promotion` alone does not count) is a 400 `missing_required_field` when it is the only update, and is ignored (no creative rebuild) next to another updatable field.  **TikTok**: patch-style. Pass any subset.  - `headline` is ignored (no headline slot). - `body` becomes the in-feed `ad_text`; `linkUrl` becomes `landing_page_url`; `videoUrl` triggers a fresh upload. - `description`, `videoId` and `existingCreativeId` are Meta-only and return 400.  **LinkedIn**: requires new media (image via `imageUrl` or video via `videoUrl`); a text-only update returns 400.  - Uploads the media, creates a new inline media creative on the same campaign, and removes the old creative. `platformAdId` and `creative.creativeId` move to the new one. - The new creative keeps the old one's state. A `DRAFT` or `PAUSED` creative is re-created `DRAFT`, because LinkedIn refuses `PAUSED` before review is `APPROVED`. - If the old creative cannot be removed, the new one is deleted and the LinkedIn error is returned. - `videoId` and `existingCreativeId` are Meta-only and return 400. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**promotion** | **Object** | Not supported. Send null or omit the field, and set the Promotion on the ad in Ads Manager. Any object is rejected with 400 invalid_field_value.  Meta validates creative_sourcing_spec.promotion_metadata_spec on the create call and then discards it, so a Promotion set through the Marketing API never reaches the creative. Verified on 2026-09-11 across Graph v19.0 to v25.0 and every write path.  |  [optional] |
|**creativeFeatures** | [**Map&lt;String, InnerEnum&gt;**](#Map&lt;String, InnerEnum&gt;) | Meta Advantage+ creative enhancements. Map snake_case feature names to OPT_IN or OPT_OUT; Meta validates supported keys. On creation Zernio sends only the keys you name, so Meta&#39;s default applies to the rest; on PUT /v1/ads/{adId} omitted keys keep the creative&#39;s current value. Send OPT_OUT to switch an enhancement off.  auto_promotion_tag is an Advantage+ enhancement, not the Ads Manager Promotion setting. The deprecated standard_enhancements bundle (subcode 3858504) is a 400 before any Meta call.  |  [optional] |
|**catalogFormat** | [**CatalogFormatEnum**](#CatalogFormatEnum) | Meta catalog template ads only. Rebuilds the creative with this &#x60;template_data.format_option&#x60; (same mapping as on create) and repoints the ad at the new creative.  Returns 400 on any other network, on a Meta ad without a catalog template creative, or with &#x60;existingCreativeId&#x60;. Copy or media fields return 422 on a catalog creative. |  [optional] |
|**headline** | **String** | Meta and LinkedIn (TikTok has no headline slot) |  [optional] |
|**longHeadline** | **String** | Google Display only. Replaces the responsive display ad&#39;s long headline. |  [optional] |
|**businessName** | **String** | Google Display only. Replaces the responsive display ad&#39;s business name. |  [optional] |
|**squareImageUrl** | **URI** | Google Display only. Uploaded as a new square (1:1) marketing image asset that replaces the current one. |  [optional] |
|**body** | **String** | Primary text. On a Meta asset_feed creative it replaces the feed&#39;s only body option (422 when it has several: send &#x60;bodies&#x60;). |  [optional] |
|**bodies** | **List&lt;String&gt;** | Meta only. The primary text options of an asset_feed creative, one text per option in the order GET /v1/ads/{adId} returns them. Each replaces the option in its position and keeps its rule. A different count returns 422, as does a single-text creative (send &#x60;body&#x60;). Not with &#x60;body&#x60;. |  [optional] |
|**headlines** | **List&lt;String&gt;** | Meta only. Same as &#x60;bodies&#x60;, for the headline options (Meta &#x60;asset_feed_spec.titles&#x60;). Cannot be sent with &#x60;headline&#x60;. Not the top-level Google &#x60;headlines&#x60;. |  [optional] |
|**description** | **String** | Link description slot (Meta &#x60;link_data.description&#x60; / &#x60;video_data.link_description&#x60;, LinkedIn creative description). |  [optional] |
|**descriptions** | **List&lt;String&gt;** | Meta only. Same as &#x60;bodies&#x60;, for the description options. Cannot be sent with &#x60;description&#x60;. Not the top-level Google &#x60;descriptions&#x60;. |  [optional] |
|**callToAction** | **String** |  |  [optional] |
|**linkUrl** | **URI** |  |  [optional] |
|**imageUrl** | **URI** |  |  [optional] |
|**videoUrl** | **URI** |  |  [optional] |
|**videoId** | **String** | Meta only. Reuse an already-uploaded ad video (from POST /v1/ads/videos or GET /v1/ads/videos) instead of re-uploading via videoUrl. |  [optional] |
|**existingCreativeId** | **String** | Meta only. Repoint the ad at an existing library creative (from GET /v1/ads/creatives); all other creative fields are ignored. |  [optional] |



## Enum: Map&lt;String, InnerEnum&gt;

| Name | Value |
|---- | -----|
| OPT_IN | &quot;OPT_IN&quot; |
| OPT_OUT | &quot;OPT_OUT&quot; |



## Enum: CatalogFormatEnum

| Name | Value |
|---- | -----|
| SINGLE_IMAGE | &quot;single_image&quot; |
| CAROUSEL_IMAGES_MULTI_ITEMS | &quot;carousel_images_multi_items&quot; |
| CAROUSEL_IMAGES_SINGLE_ITEM | &quot;carousel_images_single_item&quot; |
| CAROUSEL_SLIDESHOWS | &quot;carousel_slideshows&quot; |



