

# OnSmsRegistrationStatusUpdatedRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
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



