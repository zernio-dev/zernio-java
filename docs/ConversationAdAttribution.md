

# ConversationAdAttribution

The ad that opened the conversation, enriched from the ads Zernio syncs for the account owner. null when the conversation did not start from a Meta referral (ad click or ig.me / m.me ref link).  Meta's referral carries the ad ID but no campaign or ad set ID. When the ad is in your synced ads (`GET /v1/ads`), `synced` is true and the ad name, campaign, ad set and ad account come from there. Otherwise `synced` is false, `name` falls back to the ad title (Instagram, Facebook) or headline (WhatsApp) Meta sent with the click, and the other fields are null.  A team member limited to some profiles, or an API key scoped to profiles, is enriched only from the ads it can list with `GET /v1/ads`; any other ad comes back `synced` false.  A non-null object with `adId` null is a referral that is not an ad click: an ig.me / m.me ref link (`name` null) or a WhatsApp click on a post (`ctwa_source_type` post, `name` is Meta's headline). Nothing is looked up in your ads for it and `synced` is false. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **String** | Meta&#39;s ad ID: &#x60;meta_ad_id&#x60; on Instagram and Facebook, &#x60;ctwa_source_id&#x60; on WhatsApp when &#x60;ctwa_source_type&#x60; is &#x60;ad&#x60;. Accepted by &#x60;GET /v1/ads/{adId}&#x60;. |  |
|**name** | **String** | The synced ad&#39;s name, else the ad title or headline Meta sent. |  |
|**synced** | **Boolean** | True when the ad was found in your synced ads. |  |
|**campaignId** | **String** | Meta campaign ID. Synced ads only. |  |
|**campaignName** | **String** | Campaign name. Synced ads only. |  |
|**adSetId** | **String** | Meta ad set ID. Synced ads only. |  |
|**adSetName** | **String** | Ad set name. Synced ads only. |  |
|**adAccountId** | **String** | Meta ad account ID (act_...). Synced ads only. |  |
|**adAccountName** | **String** | Ad account name. Synced ads only. |  |
|**platformPostId** | **String** | The post the ad promotes, from the synced ad or else Meta&#39;s &#x60;post_id&#x60; on the click. |  |
|**isExternal** | **Boolean** | True when the ad was created outside Zernio (synced from Ads Manager), false when created through Zernio, null when not synced. |  |



