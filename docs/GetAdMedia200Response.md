

# GetAdMedia200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **String** |  |  [optional] |
|**platform** | **String** | &#39;facebook&#39; or &#39;instagram&#39;. Only Meta is supported for now. |  [optional] |
|**synced** | **Boolean** | False when the ad was read live from Meta because it is not in Zernio&#39;s store (request made with &#x60;accountId&#x60;). |  [optional] |
|**media** | [**List&lt;GetAdMedia200ResponseMediaInner&gt;**](GetAdMedia200ResponseMediaInner.md) |  |  [optional] |



