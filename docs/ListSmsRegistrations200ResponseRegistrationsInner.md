

# ListSmsRegistrations200ResponseRegistrationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**registrationType** | [**RegistrationTypeEnum**](#RegistrationTypeEnum) |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | requested/changes_requested &#x3D; pre-submission review states; customers see them as pending / needs changes. |  [optional] |
|**brandStatus** | **String** | Carrier-registry brand status (e.g. VERIFIED). |  [optional] |
|**campaignStatus** | **String** |  |  [optional] |
|**brandId** | **String** | TCR brand id, useful when referencing the brand in carrier support threads. |  [optional] |
|**campaignId** | **String** | TCR campaign id. |  [optional] |
|**declineReason** | **String** |  |  [optional] |
|**tfActionRequiredAt** | **OffsetDateTime** | Toll-free only: when the carrier requested changes (\&quot;Waiting For Customer\&quot;). The request must be resubmitted within 7 days of this timestamp or it expires. |  [optional] |
|**phoneNumbers** | **List&lt;String&gt;** |  |  [optional] |
|**awaitingOtp** | **Boolean** | Sole-prop 10DLC only; the OTP step is still pending. |  [optional] |
|**adminReviewNote** | **String** | The open change request as text (status changes_requested). |  [optional] |
|**lastResponseAt** | **OffsetDateTime** | When you last answered a change request. |  [optional] |
|**previouslyRejected** | **Boolean** | Rejected by the carriers at least once. A pending registration with this set is our fix, back with the carriers. |  [optional] |
|**lastRejectedAt** | **OffsetDateTime** | When the carriers last rejected it. |  [optional] |
|**rejectedBeforeSubmission** | **Boolean** | Rejected in our review before anything was filed with the carriers (not a carrier rejection; nothing to fix or appeal). |  [optional] |
|**otpExpired** | **Boolean** | Sole proprietor only: the verification code was never entered within 30 days. Start SMS setup again; it revives the same brand with no second brand fee. |  [optional] |
|**reviewRequest** | [**SmsRegistrationReviewRequest**](SmsRegistrationReviewRequest.md) |  |  [optional] |
|**trustScore** | **BigDecimal** | Carrier-assigned brand trust score; drives throughput. |  [optional] |
|**throughput** | [**ListSmsRegistrations200ResponseRegistrationsInnerThroughput**](ListSmsRegistrations200ResponseRegistrationsInnerThroughput.md) |  |  [optional] |



## Enum: RegistrationTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_10DLC | &quot;standard_10dlc&quot; |
| SOLE_PROP_10DLC | &quot;sole_prop_10dlc&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |
| REQUESTED | &quot;requested&quot; |
| CHANGES_REQUESTED | &quot;changes_requested&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



