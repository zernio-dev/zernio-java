

# WebhookPayloadMessageMetadataReferral

Click attribution forwarded verbatim from Meta. Populated only on the FIRST inbound message after the click; absent on subsequent messages of the same conversation. On Instagram and Messenger a RETURNING click also attaches it to the first message that follows, so read it on every `message.received` for per-click attribution; a click that opens an existing thread WITHOUT a message arrives as the separate `referral.received` event.  The populated subset identifies the source:   - `ctwa_clid` and `source_*` fields: WhatsApp CTWA     (Click-to-WhatsApp). Attribution window is 7 days from click.     Forward to Meta Conversions API for Business Messaging replay.   - `ad_id` and `ads_context_data`: Facebook Messenger CTM     (Click-to-Message) or Instagram CTD (Click-to-Direct). Use     `ad_id` to attribute the conversation to a specific ad.   - `ref` without `ad_id`: an ig.me / m.me link carrying a     `?ref=` parameter (`source` is `SHORTLINK`, `SHORTLINKS` or     `IGME-SOURCE-LINK` depending on surface - treat it as     opaque). Instagram delivers ig.me refs on new threads only     when the account has at least one Ice Breaker configured     (`PUT /v1/accounts/{accountId}/instagram-ice-breakers`). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ctwaClid** | **String** | Meta&#39;s GCLID-equivalent click identifier. |  [optional] |
|**sourceId** | **String** |  |  [optional] |
|**sourceType** | **String** |  |  [optional] |
|**sourceUrl** | **String** |  |  [optional] |
|**headline** | **String** |  |  [optional] |
|**body** | **String** |  |  [optional] |
|**mediaType** | **String** |  |  [optional] |
|**imageUrl** | **String** |  |  [optional] |
|**videoUrl** | **String** |  |  [optional] |
|**thumbnailUrl** | **String** |  |  [optional] |
|**adId** | **String** | Facebook Messenger CTM / Instagram CTD only. The Meta ad ID the user clicked to start the conversation.  |  [optional] |
|**ref** | **String** | The &#x60;ref&#x60; parameter passed through from the Meta ad creative or from an ig.me / m.me link. Instagram / Facebook Messenger only.  |  [optional] |
|**source** | **String** | Meta-supplied source identifier (&#x60;ADS&#x60; for ad clicks; &#x60;SHORTLINK&#x60;, &#x60;SHORTLINKS&#x60; or &#x60;IGME-SOURCE-LINK&#x60; for ref links). Instagram / Facebook Messenger only.  |  [optional] |
|**type** | **String** | Meta-supplied referral type (e.g. &#x60;OPEN_THREAD&#x60;). Instagram / Facebook Messenger only.  |  [optional] |
|**refererUri** | **String** | URI of the originating site, when Meta supplies one (m.me links opened from the web). Facebook Messenger only.  |  [optional] |
|**adsContextData** | [**WebhookPayloadMessageMetadataReferralAdsContextData**](WebhookPayloadMessageMetadataReferralAdsContextData.md) |  |  [optional] |



