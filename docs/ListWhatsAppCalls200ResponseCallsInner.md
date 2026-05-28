

# ListWhatsAppCalls200ResponseCallsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**from** | **String** |  |  [optional] |
|**to** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**endedAt** | **OffsetDateTime** |  |  [optional] |
|**durationSeconds** | **Integer** |  |  [optional] |
|**endReason** | [**EndReasonEnum**](#EndReasonEnum) |  |  [optional] |
|**recordingUrl** | **String** |  |  [optional] |
|**billing** | [**ListWhatsAppCalls200ResponseCallsInnerBilling**](ListWhatsAppCalls200ResponseCallsInnerBilling.md) |  |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RINGING | &quot;ringing&quot; |
| ANSWERED | &quot;answered&quot; |
| ENDED | &quot;ended&quot; |
| FAILED | &quot;failed&quot; |



## Enum: EndReasonEnum

| Name | Value |
|---- | -----|
| HANGUP | &quot;hangup&quot; |
| NO_ANSWER | &quot;no_answer&quot; |
| REJECTED | &quot;rejected&quot; |
| ERROR | &quot;error&quot; |



