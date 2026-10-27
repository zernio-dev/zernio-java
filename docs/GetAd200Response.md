

# GetAd200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ad** | [**Ad**](Ad.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | Google RSA details cache timestamp. |  [optional] |
|**stale** | **Boolean** | Whether Google RSA details use the last successful cached response. |  [optional] |
|**statusReadAt** | **OffsetDateTime** | With &#x60;live&#x3D;true&#x60;, when the switches were read from the platform; null when the live read failed and the stored values were returned. Always set on an unsynced Meta ad read with &#x60;accountId&#x60;, the time of that read. |  [optional] |
|**darkPost** | [**GetAd200ResponseDarkPost**](GetAd200ResponseDarkPost.md) |  |  [optional] |



