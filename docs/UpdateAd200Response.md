

# UpdateAd200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**validateOnly** | **Boolean** | Present and true when the request was sent with validateOnly: nothing was changed. The other fields of a real update are then absent. |  [optional] |
|**results** | [**List&lt;AdWriteValidationResult&gt;**](AdWriteValidationResult.md) | validateOnly only: one entry, the object Meta validated. |  [optional] |
|**ad** | [**Ad**](Ad.md) |  |  [optional] |
|**message** | **String** |  |  [optional] |



