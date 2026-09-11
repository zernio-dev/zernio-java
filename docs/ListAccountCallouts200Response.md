

# ListAccountCallouts200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** |  |  [optional] |
|**callouts** | [**List&lt;ListAccountCallouts200ResponseCalloutsInner&gt;**](ListAccountCallouts200ResponseCalloutsInner.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | Time of the cached Google read. Null when no cache was used. |  [optional] |
|**stale** | **Boolean** | True when exhausted quota required returning the last successful read. |  [optional] |



