

# GetAdsSearchTerms200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** |  |  [optional] |
|**data** | [**List&lt;GetAdsSearchTerms200ResponseDataInner&gt;**](GetAdsSearchTerms200ResponseDataInner.md) |  |  [optional] |
|**paging** | [**GetAdsSearchTerms200ResponsePaging**](GetAdsSearchTerms200ResponsePaging.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this data was fetched from Google. Null when it was never served from cache. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s daily API quota was exhausted and this is the last successful fetch, not a live read. |  [optional] |



