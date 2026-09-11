

# SubmitPhoneNumberKyc200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**preOrder** | **Boolean** | True when nothing was in stock and this submission placed a pre-order. The number stays &#x60;pending_regulatory&#x60; until we get it, from regular stock the moment it returns or sourced by the carrier (usually 2 to 4 weeks), and is not billed until active. Releasing it (DELETE /v1/phone-numbers/{id}) cancels the pre-order. A pre-order is one number: &#x60;quantity&#x60; above 1 is rejected with 400. |  [optional] |
|**phoneNumber** | [**SubmitPhoneNumberKyc200ResponsePhoneNumber**](SubmitPhoneNumberKyc200ResponsePhoneNumber.md) |  |  [optional] |
|**numbers** | [**List&lt;SubmitPhoneNumberKyc200ResponseNumbersInner&gt;**](SubmitPhoneNumberKyc200ResponseNumbersInner.md) | Every number provisioned from this submission. Length equals the requested &#x60;quantity&#x60; on full success (fewer if some orders failed; best-effort). The first element mirrors &#x60;phoneNumber&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| KYC_SUBMITTED | &quot;kyc_submitted&quot; |
| KYC_REUSED | &quot;kyc_reused&quot; |
| KYC_ALREADY_SUBMITTED | &quot;kyc_already_submitted&quot; |



