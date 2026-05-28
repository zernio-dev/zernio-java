

# WebhookPayloadCallEndedCall


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**metaCallId** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**phoneNumberId** | **String** |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**from** | **String** |  |  [optional] |
|**to** | **String** |  |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**endedAt** | **OffsetDateTime** |  |  [optional] |
|**durationSeconds** | **Integer** |  |  [optional] |
|**endReason** | [**EndReasonEnum**](#EndReasonEnum) |  |  [optional] |
|**recordingUrl** | **String** |  |  [optional] |
|**recordingExpiresAt** | **OffsetDateTime** |  |  [optional] |
|**billing** | [**WebhookPayloadCallEndedCallBilling**](WebhookPayloadCallEndedCallBilling.md) |  |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



## Enum: EndReasonEnum

| Name | Value |
|---- | -----|
| HANGUP | &quot;hangup&quot; |
| NO_ANSWER | &quot;no_answer&quot; |
| REJECTED | &quot;rejected&quot; |
| ERROR | &quot;error&quot; |



