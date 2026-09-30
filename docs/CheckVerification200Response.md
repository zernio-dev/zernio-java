

# CheckVerification200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  [optional] |
|**to** | **String** |  |  [optional] |
|**expiresAt** | **OffsetDateTime** |  |  [optional] |
|**attempts** | **Integer** |  |  [optional] |
|**maxAttempts** | **Integer** |  |  [optional] |
|**sendCount** | **Integer** | Accepted deliveries (initial send + resends); each bills one verification fee. |  [optional] |
|**lastSentAt** | **OffsetDateTime** |  |  [optional] |
|**deliveryStatus** | [**DeliveryStatusEnum**](#DeliveryStatusEnum) | WhatsApp only, returned by GET /v1/verify/verifications/{verificationId} (null on create and check responses): what Meta reported for the latest send, null until it reports. A code that never reached the recipient (for example a number not on WhatsApp) reads failed, with the Meta error in deliveryErrorCode. failed does not settle the verification: Meta can report failed and later deliver the same message. Reported for at least an hour after the send, well past any code&#39;s expiry. |  [optional] |
|**deliveryErrorCode** | **Integer** | Meta error code when deliveryStatus is failed (e.g. 131026, message undeliverable). |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**resend** | **Boolean** | Present on create responses: true when an active verification was resent instead of created. |  [optional] |
|**valid** | **Boolean** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| EXPIRED | &quot;expired&quot; |
| MAX_ATTEMPTS_REACHED | &quot;max_attempts_reached&quot; |
| CANCELED | &quot;canceled&quot; |
| DELIVERY_FAILED | &quot;delivery_failed&quot; |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |
| WHATSAPP | &quot;whatsapp&quot; |



## Enum: DeliveryStatusEnum

| Name | Value |
|---- | -----|
| DELIVERED | &quot;delivered&quot; |
| READ | &quot;read&quot; |
| FAILED | &quot;failed&quot; |



