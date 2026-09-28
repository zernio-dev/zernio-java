

# OnBrandedCallingIdentityStatusUpdatedRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**identity** | [**OnBrandedCallingIdentityStatusUpdatedRequestIdentity**](OnBrandedCallingIdentityStatusUpdatedRequestIdentity.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**reason** | **String** | Our review note, or the carrier&#39;s rejection reasons, when there is one. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| BRANDED_CALLING_IDENTITY_STATUS_UPDATED | &quot;branded_calling.identity.status_updated&quot; |



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



