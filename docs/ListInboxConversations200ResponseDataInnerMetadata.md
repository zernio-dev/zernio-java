

# ListInboxConversations200ResponseDataInnerMetadata

Click attribution for a conversation that started from a Meta ad or a ref-tagged ig.me / m.me link. Absent when the conversation did not originate from an attributable click.  Captured from the referral Meta delivers for the click. If the same person later arrives through a different ad or link, the original values are kept, so the first referral wins; read the fresh referral per click on the `message.received` / `referral.received` webhooks instead. One exception on WhatsApp: when Meta omits `ctwa_clid` from that referral, a later Meta automatic event can supply it and refresh `ctwa_captured_at`, so treat `ctwa_captured_at` as the time Zernio stored the value, not the time of the click.  Two families of keys, one per surface. They never appear together:    - `ctwa_*` is WhatsApp Click-to-WhatsApp. The ad ID is     `ctwa_source_id`. There is no `meta_ad_id` on WhatsApp.   - `meta_ad_*` is Instagram Click-to-Direct, Facebook Messenger     Click-to-Message, and ig.me / m.me ref links. The ad ID is     `meta_ad_id` (ad clicks only; a link capture carries     `meta_ad_ref` without it). `ctwa_clid` never appears on these     platforms.  Every key is optional and only the keys Meta supplied are returned, so read defensively. Meta does not send a campaign or ad set ID, so none is exposed here. More keys may be added over time. Treat any key you do not recognise as an opaque string.  Key names differ from the `message.received` webhook on purpose. The webhook forwards Meta's referral verbatim (`ad_id`, `source`, `type`) while the stored conversation record uses the prefixed names below. Renaming either side would break existing integrations, so both spellings are kept. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ctwaClid** | **String** | WhatsApp only. Meta&#39;s click identifier, the value to forward to the Meta Conversions API for Business Messaging. Meta omits it on some numbers, so a WhatsApp referral can arrive without it. |  [optional] |
|**ctwaSourceId** | **String** | WhatsApp only. The Meta ad ID the user clicked. This is the WhatsApp equivalent of meta_ad_id. |  [optional] |
|**ctwaSourceType** | **String** | WhatsApp only. What the user clicked, as supplied by Meta (for example ad or post). |  [optional] |
|**ctwaSourceUrl** | **String** | WhatsApp only. Meta&#39;s URL for the ad that was clicked, normally an fb.me short link. |  [optional] |
|**ctwaHeadline** | **String** | WhatsApp only. Headline of the ad creative at click time. |  [optional] |
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



