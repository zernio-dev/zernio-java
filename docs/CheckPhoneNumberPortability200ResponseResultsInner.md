

# CheckPhoneNumberPortability200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumber** | **String** |  |  [optional] |
|**portable** | **Boolean** |  |  [optional] |
|**fastPortable** | **Boolean** | Qualifies for the carrier&#39;s accelerated FastPort lane. |  [optional] |
|**messagingCapable** | **Boolean** | Whether texting can be enabled on the number once ported; null when the carrier does not say. |  [optional] |
|**lineType** | **String** | Line type when known (mobile, landline, voip, toll-free, unknown). US/CA portable numbers only. A US/CA mobile number requires the transfer PIN at submit. |  [optional] |
|**carrierName** | **String** | The number&#39;s current carrier, when the lookup knows it. US/CA portable numbers only. |  [optional] |
|**countryCode** | **String** | ISO country of the number. Pass it to GET /v1/phone-numbers/port-in/requirements for international numbers. |  [optional] |
|**phoneNumberType** | **String** | Carrier number-type classification (local, mobile, national, toll_free...), the numberType for the requirements endpoint. |  [optional] |
|**notPortableReason** | **String** | Carrier reason when not portable; null when portable. |  [optional] |
|**claimId** | **String** | Keyless calls and claimLinks&#x3D;true only, on portable results. Resolve it with GET /v1/phone-numbers/port-in/claims/{claimId}. Expires after 7 days. |  [optional] |
|**claimUrl** | **String** | Keyless calls and claimLinks&#x3D;true only, on portable results. A signup link that lands on the dashboard&#39;s port form with this number filled in. |  [optional] |



