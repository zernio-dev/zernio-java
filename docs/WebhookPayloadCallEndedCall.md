

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
|**hangupCause** | **String** | Raw carrier hangup cause behind endReason (e.g. normal_clearing, call_rejected, not_found). Null when the carrier reported none. |  [optional] |
|**sipHangupCause** | **String** | SIP response code that ended the call when SIP-signalled (e.g. &#39;403&#39;, &#39;486&#39;, &#39;603&#39;). endReason collapses all three to &#39;rejected&#39;, so this is what separates a refused destination from a busy line. Null on non-SIP legs. |  [optional] |
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



