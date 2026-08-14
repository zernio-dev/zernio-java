

# WebhookPayloadReferralReferral

Meta's referral object, forwarded verbatim. Same shape as `metadata.referral` on `message.received`: `ref` + `source` for ig.me / m.me links, `ad_id` + `ads_context_data` for returning Messenger ad clicks. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ref** | **String** | The &#x60;ref&#x60; parameter of the clicked ig.me / m.me link or ad. |  [optional] |
|**source** | **String** | Meta-supplied source (&#x60;SHORTLINK&#x60;, &#x60;SHORTLINKS&#x60;, &#x60;IGME-SOURCE-LINK&#x60;, &#x60;ADS&#x60; - treat as opaque). |  [optional] |
|**type** | **String** | Meta-supplied referral type (e.g. &#x60;OPEN_THREAD&#x60;). |  [optional] |
|**refererUri** | **String** | URI of the originating site, when Meta supplies one. Facebook Messenger only. |  [optional] |
|**adId** | **String** | The Meta ad ID, on returning ad clicks. Facebook Messenger only. |  [optional] |
|**adsContextData** | [**WebhookPayloadReferralReferralAdsContextData**](WebhookPayloadReferralReferralAdsContextData.md) |  |  [optional] |



