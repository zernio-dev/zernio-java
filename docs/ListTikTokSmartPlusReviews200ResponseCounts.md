

# ListTikTokSmartPlusReviews200ResponseCounts

The Smart+ ads on this page split by state; the four counts add up to the Smart+ ads on this page (fewer than `pageSize` on the last page).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fresh** | **Integer** | Items read within &#x60;maxAgeSeconds&#x60;. |  [optional] |
|**stale** | **Integer** | Items read earlier, returned with their &#x60;readAt&#x60; and due for a refresh. |  [optional] |
|**pending** | **Integer** | Smart+ ads never read (&#x60;pendingSmartPlusAdIds&#x60;). |  [optional] |
|**failed** | **Integer** | Entries of &#x60;failedSmartPlusAds&#x60;. |  [optional] |



