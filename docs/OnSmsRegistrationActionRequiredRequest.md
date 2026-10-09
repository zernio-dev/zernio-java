

# OnSmsRegistrationActionRequiredRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**registration** | [**OnSmsRegistrationActionRequiredRequestRegistration**](OnSmsRegistrationActionRequiredRequestRegistration.md) |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  [optional] |
|**message** | **String** | What to do, in words: our request or the carrier&#39;s note. Absent for otp_required. |  [optional] |



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



