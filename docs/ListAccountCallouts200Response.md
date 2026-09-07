

# ListAccountCallouts200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** |  |  [optional] |
|**callouts** | [**List&lt;ListAccountCallouts200ResponseCalloutsInner&gt;**](ListAccountCallouts200ResponseCalloutsInner.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this list was fetched from Google. Null when it was never served from cache. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s daily API quota was exhausted and this is the last successful fetch, not a live read. |  [optional] |



