

# BrandedCallingIdentity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**enterpriseId** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**callReasons** | **List&lt;String&gt;** |  |  [optional] |
|**callReasonsPreApproved** | **Boolean** | Every call reason matches the carrier catalogue (GET /v1/branded-calling/call-reasons); anything else is vetted by hand and takes longer. |  [optional] |
|**logoUrl** | **String** | The image you sent. Zernio hosts the 256x256 BMP the carriers require. |  [optional] |
|**authorizer** | [**BrandedCallingIdentityAuthorizer**](BrandedCallingIdentityAuthorizer.md) |  |  [optional] |
|**references** | [**BrandedCallingReferences**](BrandedCallingReferences.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | requested &#x3D; in Zernio review; changes_requested &#x3D; answer the review (PATCH); pending_email_verification &#x3D; confirm the code emailed to the authorizer; in_review &#x3D; with the carrier vetting team; verified &#x3D; attach numbers; rejected &#x3D; fix and PATCH to resubmit; suspended &#x3D; an infringement claim is open; expired &#x3D; the yearly verification lapsed; permanently_rejected &#x3D; terminal. |  [optional] |
|**rejectionReasons** | [**List&lt;BrandedCallingIdentityRejectionReasonsInner&gt;**](BrandedCallingIdentityRejectionReasonsInner.md) |  |  [optional] |
|**reviewNote** | **String** | The open change request, as text. |  [optional] |
|**reviewRequest** | [**BrandedCallingIdentityReviewRequest**](BrandedCallingIdentityReviewRequest.md) |  |  [optional] |
|**emailVerifiedAt** | **OffsetDateTime** |  |  [optional] |
|**submittedAt** | **OffsetDateTime** |  |  [optional] |
|**verifiedAt** | **OffsetDateTime** |  |  [optional] |
|**expiringAt** | **OffsetDateTime** | Verification lasts one year; Zernio resubmits 30 days before this date. |  [optional] |
|**numbers** | [**List&lt;BrandedCallingIdentityNumber&gt;**](BrandedCallingIdentityNumber.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| REQUESTED | &quot;requested&quot; |
| CHANGES_REQUESTED | &quot;changes_requested&quot; |
| REJECTED | &quot;rejected&quot; |
| PENDING_EMAIL_VERIFICATION | &quot;pending_email_verification&quot; |
| IN_REVIEW | &quot;in_review&quot; |
| VERIFIED | &quot;verified&quot; |
| SUSPENDED | &quot;suspended&quot; |
| EXPIRED | &quot;expired&quot; |
| PERMANENTLY_REJECTED | &quot;permanently_rejected&quot; |



