

# GetPhoneNumberKycForm200ResponseReusableOptionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Opaque option id — pass as &#x60;reuseOptionId&#x60; on POST. Stable selection key (a phone number is not unique across verifications). |  [optional] |
|**fromPhoneNumber** | **String** | Display only — the number this verification was submitted for. Not a selection key. |  [optional] |
|**instant** | **Boolean** | true &#x3D; group-approved, a new order activates in minutes; false &#x3D; documents are reused but the order still queues for carrier review (1-3 days). |  [optional] |
|**details** | [**List&lt;GetPhoneNumberKycForm200ResponseReusableOptionsInnerDetailsInner&gt;**](GetPhoneNumberKycForm200ResponseReusableOptionsInnerDetailsInner.md) |  |  [optional] |



