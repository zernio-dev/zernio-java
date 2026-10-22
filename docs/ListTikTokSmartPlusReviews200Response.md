

# ListTikTokSmartPlusReviews200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** |  |  [optional] |
|**includeDeleted** | **Boolean** |  |  [optional] |
|**page** | **Integer** |  |  [optional] |
|**pageSize** | **Integer** |  |  [optional] |
|**totalPages** | **Integer** |  |  [optional] |
|**totalSmartPlusAds** | **Integer** | Smart+ ads of the advertiser across all pages. |  [optional] |
|**items** | [**List&lt;ListTikTokSmartPlusReviews200ResponseItemsInner&gt;**](ListTikTokSmartPlusReviews200ResponseItemsInner.md) |  |  [optional] |
|**failedSmartPlusAds** | [**List&lt;ListTikTokSmartPlusReviews200ResponseFailedSmartPlusAdsInner&gt;**](ListTikTokSmartPlusReviews200ResponseFailedSmartPlusAdsInner.md) | Smart+ ads of this page whose review TikTok refused on its own (for example an ad deleted on TikTok since the listing was cached). Zernio splits a refused batch in halves (at most 16 extra calls per page), so the other ads of the batch are still read; ads left unresolved by that cap carry the batch error. Empty when none. |  [optional] |
|**incomplete** | **Boolean** | True when some Smart+ ads of this page could not be read because of TikTok&#39;s review quota. |  [optional] |
|**pendingSmartPlusAdIds** | **List&lt;String&gt;** | Smart+ ads of this page still to read. Empty when complete. |  [optional] |
|**retryAfterSeconds** | **Integer** | Seconds to wait before reading this page again. Null when complete. |  [optional] |



