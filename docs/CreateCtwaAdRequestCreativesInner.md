

# CreateCtwaAdRequestCreativesInner

Each entry must also include exactly one of `imageUrl` or `video`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headline** | **String** |  |  |
|**body** | **String** | Primary text shown above the image / video. |  |
|**imageUrl** | **URI** | Image asset. Mutually exclusive with this entry&#39;s &#x60;video&#x60;. Required if &#x60;video&#x60; is not supplied.  |  [optional] |
|**video** | [**CreateCtwaAdRequestCreativesInnerVideo**](CreateCtwaAdRequestCreativesInnerVideo.md) |  |  [optional] |



