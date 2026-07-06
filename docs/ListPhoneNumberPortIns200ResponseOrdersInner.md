

# ListPhoneNumberPortIns200ResponseOrdersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**telnyxStatusValue** | **String** | Raw carrier status string. |  [optional] |
|**phoneNumbers** | **List&lt;String&gt;** |  |  [optional] |
|**fastPortEligible** | **Boolean** |  |  [optional] |
|**focDatetimeRequested** | **OffsetDateTime** |  |  [optional] |
|**focDatetimeActual** | **OffsetDateTime** |  |  [optional] |
|**declineReason** | **String** |  |  [optional] |
|**submittedAt** | **OffsetDateTime** |  |  [optional] |
|**portedAt** | **OffsetDateTime** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| PENDING | &quot;pending&quot; |
| FOC_CONFIRMED | &quot;foc_confirmed&quot; |
| PORTED | &quot;ported&quot; |
| EXCEPTION | &quot;exception&quot; |
| CANCELLED | &quot;cancelled&quot; |



