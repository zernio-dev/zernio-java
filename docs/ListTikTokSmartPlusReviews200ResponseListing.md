

# ListTikTokSmartPlusReviews200ResponseListing

The Smart+ ad listing this page was cut from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**readAt** | **OffsetDateTime** | When the listing was read from TikTok. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | &#x60;fresh&#x60;: read within &#x60;maxAgeSeconds&#x60;. &#x60;fallback&#x60;: relisting failed and this is the older stored listing. |  [optional] |
|**error** | [**ListTikTokSmartPlusReviews200ResponseListingError**](ListTikTokSmartPlusReviews200ResponseListingError.md) |  |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| FRESH | &quot;fresh&quot; |
| FALLBACK | &quot;fallback&quot; |



