

# OnSmsRegistrationActionRequiredRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**registration** | [**OnSmsRegistrationActionRequiredRequestRegistration**](OnSmsRegistrationActionRequiredRequestRegistration.md) |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  [optional] |
|**message** | **String** | What to do, in words: the reviewer&#39;s note or the carrier&#39;s decline reason. Absent for otp_required. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| SMS_REGISTRATION_ACTION_REQUIRED | &quot;sms.registration.action_required&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| CHANGES_REQUESTED | &quot;changes_requested&quot; |
| OTP_REQUIRED | &quot;otp_required&quot; |
| CARRIER_INFO_REQUIRED | &quot;carrier_info_required&quot; |
| REJECTED | &quot;rejected&quot; |



