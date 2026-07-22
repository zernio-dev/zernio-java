

# OnVerificationFailedRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** |  |  [optional] |
|**verification** | [**OnVerificationFailedRequestVerification**](OnVerificationFailedRequestVerification.md) |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| VERIFICATION_FAILED | &quot;verification.failed&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| MAX_ATTEMPTS_REACHED | &quot;max_attempts_reached&quot; |



