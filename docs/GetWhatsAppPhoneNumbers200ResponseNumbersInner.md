

# GetWhatsAppPhoneNumbers200ResponseNumbersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**country** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**registrantName** | **String** | For regulated numbers, who it&#39;s registered for (company or person) — set from the submitted KYC. |  [optional] |
|**telnyxOrderId** | **String** | Present once the number order has been placed (i.e. the requirement group was approved). Absent while still in identity review. |  [optional] |
|**monthlyCents** | **Integer** | Per-country monthly price in cents ($2..$25). |  [optional] |
|**profileId** | **Object** |  |  [optional] |
|**provisionedAt** | **OffsetDateTime** |  |  [optional] |
|**metaPreverifiedId** | **String** |  |  [optional] |
|**metaVerificationStatus** | **String** |  |  [optional] |
|**onfidoVerificationUrl** | **String** | For regulated (Tier 3/4) numbers with an Onfido ID-verification step — the link to forward to the end user. Set once the order is placed; null otherwise. Poll this field after submitting KYC. |  [optional] |
|**endUserFirstName** | **String** |  |  [optional] |
|**endUserLastName** | **String** |  |  [optional] |
|**regulatoryDeclineReason** | **String** | Reviewer rejection reason when status is regulatory_declined. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_PAYMENT | &quot;pending_payment&quot; |
| PENDING_REGULATORY | &quot;pending_regulatory&quot; |
| REGULATORY_DECLINED | &quot;regulatory_declined&quot; |
| PROVISIONING | &quot;provisioning&quot; |
| VERIFYING | &quot;verifying&quot; |
| ACTIVE | &quot;active&quot; |
| SUSPENDED | &quot;suspended&quot; |
| RELEASING | &quot;releasing&quot; |
| RELEASED | &quot;released&quot; |



