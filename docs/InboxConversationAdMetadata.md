

# InboxConversationAdMetadata

Click attribution for a conversation that started from a Meta ad or a ref-tagged ig.me / m.me link, as Meta sent it. Absent when the conversation did not come from an attributable click. For the ad name, campaign and ad set, read `adAttribution`.  **First referral wins.** Values come from the referral Meta delivers for the click. If the same person later arrives through another ad or link, the original values are kept. For the fresh referral per click, read the `message.received` / `referral.received` webhooks.  On Instagram Click-to-Direct, Meta usually delivers the ad post first as an attachment-only `share` / `ig_post` message with no referral, then attaches the referral to the next message.  WhatsApp exception: when Meta omits `ctwa_clid` from the referral, a later Meta automatic event can supply it and refresh `ctwa_captured_at`. Treat `ctwa_captured_at` as when Zernio stored the value, not when the click happened.  **Two key families, one per surface, never together:**  - `ctwa_*`: WhatsApp Click-to-WhatsApp. The ad ID is `ctwa_source_id`. There is no `meta_ad_id` on WhatsApp. - `meta_ad_*`: Instagram Click-to-Direct, Facebook Messenger Click-to-Message, and ig.me / m.me ref links. The ad ID is `meta_ad_id` (ad clicks only; a link capture carries `meta_ad_ref` without it). `ctwa_clid` never appears here.  Every key is optional and only keys Meta supplied are returned, so read defensively. Meta sends no campaign or ad set ID; those are resolved from your synced ads in `adAttribution`. More keys may be added; treat unknown keys as opaque strings.  Key names differ from the `message.received` webhook on purpose. The webhook forwards Meta's referral verbatim (`ad_id`, `source`, `type`), while the stored conversation uses the prefixed names. Renaming either side would break existing integrations, so both spellings stay. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ctwaClid** | **String** | WhatsApp only. Meta&#39;s click identifier, the value to forward to the Meta Conversions API for Business Messaging. Meta omits it on some numbers, so a WhatsApp referral can arrive without it. |  [optional] |
|**ctwaSourceId** | **String** | WhatsApp only. The Meta ad ID the user clicked (or the post ID when &#x60;ctwa_source_type&#x60; is post). This is the WhatsApp equivalent of meta_ad_id. |  [optional] |
|**ctwaSourceType** | **String** | WhatsApp only. What the user clicked, as supplied by Meta (for example ad or post). |  [optional] |
|**ctwaSourceUrl** | **String** | WhatsApp only. Meta&#39;s URL for the ad that was clicked, normally an fb.me short link. |  [optional] |
|**ctwaHeadline** | **String** | WhatsApp only. Headline of the ad creative at click time. |  [optional] |
|**ctwaBody** | **String** | WhatsApp only. Body text of the ad creative at click time. |  [optional] |
|**ctwaMediaType** | **String** | WhatsApp only. Media type of the ad creative, image or video. |  [optional] |
|**ctwaImageUrl** | **String** | WhatsApp only. Image of the ad creative at click time (image ads). |  [optional] |
|**ctwaVideoUrl** | **String** | WhatsApp only. Video of the ad creative at click time (video ads). |  [optional] |
|**ctwaThumbnailUrl** | **String** | WhatsApp only. Thumbnail of the ad video at click time (video ads). |  [optional] |
|**ctwaCapturedAt** | **OffsetDateTime** | WhatsApp only. When Zernio stored this referral. Always present when a WhatsApp referral was captured. |  [optional] |
|**metaAdId** | **String** | Instagram and Facebook only. The Meta ad ID the user clicked. Present for ad clicks; absent when the capture came from an ig.me / m.me ref link. |  [optional] |
|**metaAdSource** | **String** | Instagram and Facebook only. Meta-supplied source identifier: ADS for ad clicks; SHORTLINK, SHORTLINKS or IGME-SOURCE-LINK for ref links (treat as opaque). |  [optional] |
|**metaAdType** | **String** | Instagram and Facebook only. Meta-supplied referral type, for example OPEN_THREAD. |  [optional] |
|**metaAdRef** | **String** | Instagram and Facebook only. The ref parameter passed through from the ad creative or the ig.me / m.me link. |  [optional] |
|**metaAdTitle** | **String** | Instagram and Facebook only. Title of the ad creative at click time. |  [optional] |
|**metaAdPhotoUrl** | **String** | Instagram and Facebook only. Image of the ad creative at click time. |  [optional] |
|**metaAdVideoUrl** | **String** | Instagram and Facebook only. Video of the ad creative at click time. |  [optional] |
|**metaAdPostId** | **String** | Instagram and Facebook only. The organic post the ad promoted, when the ad was a boosted post. |  [optional] |
|**metaAdProductId** | **String** | Instagram and Facebook only. The catalogue product the user clicked, for product ads. |  [optional] |
|**metaAdFlowId** | **String** | Instagram and Facebook only. The Meta flow the ad launched, for flow ads. |  [optional] |
|**metaAdCapturedAt** | **OffsetDateTime** | Instagram and Facebook only. When Zernio stored this referral. Always present when an Instagram or Facebook referral was captured. |  [optional] |



