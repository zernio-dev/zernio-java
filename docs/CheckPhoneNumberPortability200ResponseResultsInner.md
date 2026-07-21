

# CheckPhoneNumberPortability200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumber** | **String** |  |  [optional] |
|**portable** | **Boolean** |  |  [optional] |
|**fastPortable** | **Boolean** | Qualifies for the carrier&#39;s accelerated FastPort lane. |  [optional] |
|**lineType** | **String** | Line type when known (mobile, landline, voip…). A US/CA mobile number requires the transfer PIN at submit. |  [optional] |
|**countryCode** | **String** | ISO country of the number — pass it to GET /v1/phone-numbers/port-in/requirements for international numbers. |  [optional] |
|**phoneNumberType** | **String** | Carrier number-type classification (local, mobile, national, toll_free…) — the numberType for the requirements endpoint. |  [optional] |
|**notPortableReason** | **String** | Carrier reason when not portable; null when portable. |  [optional] |



