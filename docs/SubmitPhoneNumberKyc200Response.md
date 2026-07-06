

# SubmitPhoneNumberKyc200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**phoneNumber** | [**SubmitPhoneNumberKyc200ResponsePhoneNumber**](SubmitPhoneNumberKyc200ResponsePhoneNumber.md) |  |  [optional] |
|**numbers** | [**List&lt;SubmitPhoneNumberKyc200ResponseNumbersInner&gt;**](SubmitPhoneNumberKyc200ResponseNumbersInner.md) | Every number provisioned from this submission. Length equals the requested &#x60;quantity&#x60; on full success (fewer if some orders failed; best-effort). The first element mirrors &#x60;phoneNumber&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| KYC_SUBMITTED | &quot;kyc_submitted&quot; |
| KYC_REUSED | &quot;kyc_reused&quot; |
| KYC_ALREADY_SUBMITTED | &quot;kyc_already_submitted&quot; |



