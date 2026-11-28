

# MetaSavedAudience

A Meta saved audience (Meta's SavedAudience node), read live from Meta.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Meta saved audience id. |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**approximateCountLowerBound** | **Integer** | Meta&#39;s estimated lower bound on reach. |  [optional] |
|**approximateCountUpperBound** | **Integer** | Meta&#39;s estimated upper bound on reach. |  [optional] |
|**runStatus** | **String** | Meta&#39;s run_status: whether the saved audience is active or deleted. |  [optional] |
|**sentenceLines** | **List&lt;Object&gt;** | Meta&#39;s human-readable targeting summary lines, passed through as Meta returns them. |  [optional] |
|**targeting** | **Map&lt;String, Object&gt;** | The Meta targeting spec saved in the audience, in Meta&#39;s own snake_case shape. Send it as &#x60;rawTargeting&#x60; on &#x60;POST /v1/ads/create&#x60; to target an ad set at this audience. |  [optional] |
|**createdAt** | **String** | Meta&#39;s time_created. |  [optional] |
|**updatedAt** | **String** | Meta&#39;s time_updated. |  [optional] |



