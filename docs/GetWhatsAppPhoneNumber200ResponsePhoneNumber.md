

# GetWhatsAppPhoneNumber200ResponsePhoneNumber


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**country** | **String** |  |  [optional] |
|**metaPreverifiedId** | **String** |  |  [optional] |
|**metaVerificationStatus** | **String** |  |  [optional] |
|**onfidoVerificationUrl** | **String** | For a regulated number with an Onfido ID step — the link to forward to the end user. Appears once the order is placed; null otherwise. |  [optional] |
|**endUserFirstName** | **String** |  |  [optional] |
|**endUserLastName** | **String** |  |  [optional] |
|**regulatoryDeclineReason** | **String** | Reviewer rejection reason when status is regulatory_declined. |  [optional] |
|**provisionedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_PAYMENT | &quot;pending_payment&quot; |
| PENDING_REGULATORY | &quot;pending_regulatory&quot; |
| REGULATORY_DECLINED | &quot;regulatory_declined&quot; |
| PROVISIONING | &quot;provisioning&quot; |
| ACTIVE | &quot;active&quot; |
| SUSPENDED | &quot;suspended&quot; |
| RELEASING | &quot;releasing&quot; |
| RELEASED | &quot;released&quot; |



