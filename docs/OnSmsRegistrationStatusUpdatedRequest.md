

# OnSmsRegistrationStatusUpdatedRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**registration** | [**OnSmsRegistrationStatusUpdatedRequestRegistration**](OnSmsRegistrationStatusUpdatedRequestRegistration.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**reason** | **String** | The carriers&#39; decline reason, on rejected. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| SMS_REGISTRATION_STATUS_UPDATED | &quot;sms.registration.status_updated&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CHANGES_REQUESTED | &quot;changes_requested&quot; |
| REQUESTED | &quot;requested&quot; |
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



