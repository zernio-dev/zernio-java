

# ListBidStrategies200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** |  |  [optional] |
|**currency** | **String** | Account currency code; money fields are in this currency&#39;s units. |  [optional] |
|**strategies** | [**List&lt;PortfolioBidStrategy&gt;**](PortfolioBidStrategy.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this data was fetched from Google. Null when it was never served from cache. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s daily API quota was exhausted and this is the last successful fetch, not a live read. |  [optional] |



