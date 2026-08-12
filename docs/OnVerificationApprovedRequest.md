

# OnVerificationApprovedRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**verification** | [**OnVerificationApprovedRequestVerification**](OnVerificationApprovedRequestVerification.md) |  |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| VERIFICATION_APPROVED | &quot;verification.approved&quot; |



