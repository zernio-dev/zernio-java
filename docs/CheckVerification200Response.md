

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



