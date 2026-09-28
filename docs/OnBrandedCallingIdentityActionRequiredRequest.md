

# OnBrandedCallingIdentityActionRequiredRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**identity** | [**OnBrandedCallingIdentityActionRequiredRequestIdentity**](OnBrandedCallingIdentityActionRequiredRequestIdentity.md) |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  [optional] |
|**message** | **String** | What to do, in words. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| BRANDED_CALLING_IDENTITY_ACTION_REQUIRED | &quot;branded_calling.identity.action_required&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| CHANGES_REQUESTED | &quot;changes_requested&quot; |
| EMAIL_CODE | &quot;email_code&quot; |
| REJECTED | &quot;rejected&quot; |
| INFRINGEMENT_CLAIM | &quot;infringement_claim&quot; |
| EXPIRED | &quot;expired&quot; |



