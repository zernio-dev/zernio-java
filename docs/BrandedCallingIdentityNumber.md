

# BrandedCallingIdentityNumber


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumberId** | **String** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | verified &#x3D; the identity shows on calls from this number. permanently_rejected cannot be attached again anywhere. |  [optional] |
|**rejectionReason** | [**BrandedCallingIdentityNumberRejectionReason**](BrandedCallingIdentityNumberRejectionReason.md) |  |  [optional] |
|**verifiedAt** | **OffsetDateTime** |  |  [optional] |
|**addedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;submitted&quot; |
| IN_REVIEW | &quot;in_review&quot; |
| VERIFIED | &quot;verified&quot; |
| UNSUCCESSFUL | &quot;unsuccessful&quot; |
| SUSPENDED | &quot;suspended&quot; |
| EXPIRED | &quot;expired&quot; |
| PERMANENTLY_REJECTED | &quot;permanently_rejected&quot; |



