

# GetAdAccountHierarchy200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**roots** | [**List&lt;GetAdAccountHierarchy200ResponseRootsInner&gt;**](GetAdAccountHierarchy200ResponseRootsInner.md) |  |  [optional] |
|**unavailable** | [**List&lt;GetAdAccountHierarchy200ResponseUnavailableInner&gt;**](GetAdAccountHierarchy200ResponseUnavailableInner.md) |  |  [optional] |
|**truncated** | **Boolean** |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this data was fetched from Google. Null on a live read. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s quota was exhausted and this is the last successful fetch. |  [optional] |



