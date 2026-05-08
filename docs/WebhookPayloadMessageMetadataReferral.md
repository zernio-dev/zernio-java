

# WebhookPayloadMessageMetadataReferral

Ad-click attribution forwarded verbatim from Meta. Populated only on the FIRST inbound message after the click; absent on subsequent messages of the same conversation.  The populated subset identifies the source platform:   - `ctwa_clid` and `source_*` fields: WhatsApp CTWA     (Click-to-WhatsApp). Attribution window is 7 days from click.     Forward to Meta Conversions API for Business Messaging replay.   - `ad_id` and `ads_context_data`: Facebook Messenger CTM     (Click-to-Message) or Instagram CTD (Click-to-Direct). Use     `ad_id` to attribute the conversation to a specific ad. 

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
|**ref** | **String** | Optional &#x60;ref&#x60; parameter passed through from the Meta ad creative. Facebook Messenger CTM / Instagram CTD only.  |  [optional] |
|**source** | **String** | Meta-supplied source identifier (e.g. &#x60;ADS&#x60;). Facebook Messenger CTM / Instagram CTD only.  |  [optional] |
|**type** | **String** | Meta-supplied referral type (e.g. &#x60;OPEN_THREAD&#x60;). Facebook Messenger CTM / Instagram CTD only.  |  [optional] |
|**adsContextData** | [**WebhookPayloadMessageMetadataReferralAdsContextData**](WebhookPayloadMessageMetadataReferralAdsContextData.md) |  |  [optional] |



