

# ListConversionActions200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** | The Google Ads customer id the actions were read from. |  [optional] |
|**actions** | [**List&lt;ConversionAction&gt;**](ConversionAction.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this list was fetched from Google. Null when it was never served from cache. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s daily API quota was exhausted and this is the last successful fetch, not a live read. |  [optional] |



