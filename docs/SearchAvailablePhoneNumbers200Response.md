

# SearchAvailablePhoneNumbers200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** |  |  [optional] |
|**numberType** | **String** |  |  [optional] |
|**requireSms** | **Boolean** | Echo of the &#x60;sms&#x60; filter applied to this search. |  [optional] |
|**numbers** | [**List&lt;SearchAvailablePhoneNumbers200ResponseNumbersInner&gt;**](SearchAvailablePhoneNumbers200ResponseNumbersInner.md) |  |  [optional] |
|**masked** | **Boolean** | true on keyless calls. |  [optional] |
|**near** | **String** | With &#x60;country&#x3D;auto&#x60;: the caller&#39;s city the results were narrowed to, or null when there was no stock there. |  [optional] |
|**claimId** | **String** | Keyless calls only: a claim for any number matching this search&#39;s country, type and area. |  [optional] |
|**claimUrl** | **String** | Keyless calls only: signup link for any number matching this search. |  [optional] |



