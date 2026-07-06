

# ListCalls200ResponseCallsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** | Owning social account. The unified /v1/calls/{id} detail + recording endpoints work for any channel; the channel-specific endpoints remain for account-scoped access. |  [optional] |
|**conversationId** | **String** | Inbox conversation with the counterparty, when one exists. |  [optional] |
|**contactId** | **String** | CRM Contact for the counterparty, when resolved. |  [optional] |
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**from** | **String** | Caller number (E.164). |  [optional] |
|**to** | **String** | Callee number (E.164). |  [optional] |
|**forwardTo** | **String** | Destination the call was routed to (tel:/sip:/wss:), snapshotted at routing time. |  [optional] |
|**greeting** | **String** | Outbound PSTN only. Message spoken to the callee on answer, before the bridge. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**isVoicemail** | **Boolean** | True when an inbound call went to voicemail. |  [optional] |
|**amd** | **Boolean** | Outbound answering-machine detection was requested for this call. |  [optional] |
|**answeredMachine** | **Boolean** | With &#x60;amd&#x60;, whether a machine (vs a human) answered. |  [optional] |
|**forwardCallerId** | [**ForwardCallerIdEnum**](#ForwardCallerIdEnum) | Caller ID presented on the forwarded leg. |  [optional] |
|**recordingEnabled** | **Boolean** | Effective flag for THIS call (number default + per-call override, resolved at create time). |  [optional] |
|**transcriptionEnabled** | **Boolean** |  |  [optional] |
|**transcriptionLanguage** | [**TranscriptionLanguageEnum**](#TranscriptionLanguageEnum) |  |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**answeredAt** | **OffsetDateTime** |  |  [optional] |
|**endedAt** | **OffsetDateTime** |  |  [optional] |
|**transferredAt** | **OffsetDateTime** | When the call was blind-transferred (POST /v1/voice/calls/{id}/transfer). |  [optional] |
|**durationSeconds** | **Integer** |  |  [optional] |
|**endReason** | [**EndReasonEnum**](#EndReasonEnum) |  |  [optional] |
|**hangupCause** | **String** | Raw carrier hangup cause behind endReason (e.g. normal_clearing, not_found, time_limit) — the actual motive when endReason is a coarse bucket. |  [optional] |
|**sipHangupCause** | **String** | SIP response code that ended the call, when SIP-signalled (e.g. &#39;403&#39;, &#39;488&#39;). The real failure reason for SIP legs. |  [optional] |
|**callErrors** | [**List&lt;CallRecordCallErrorsInner&gt;**](CallRecordCallErrorsInner.md) | Per-call failure log (dial failed, bridge failed, recording error). |  [optional] |
|**recordingUrl** | **String** | May be expired. Resolve a fresh playable URL via GET /v1/calls/{id}/recording (any channel). |  [optional] |
|**lastTranscriptSnippet** | **String** | Most recent transcript segment, for list previews. |  [optional] |
|**transcript** | [**List&lt;CallRecordTranscriptInner&gt;**](CallRecordTranscriptInner.md) | Full transcript segments (detail endpoint only; omitted from lists). |  [optional] |
|**billing** | [**CallRecordBilling**](CallRecordBilling.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**contactName** | **String** | CRM contact name for the counterparty, when resolved. |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| WHATSAPP | &quot;whatsapp&quot; |
| PSTN | &quot;pstn&quot; |



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



## Enum: ForwardCallerIdEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CALLER | &quot;caller&quot; |



## Enum: TranscriptionLanguageEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| EN | &quot;en&quot; |
| ES | &quot;es&quot; |



## Enum: EndReasonEnum

| Name | Value |
|---- | -----|
| HANGUP | &quot;hangup&quot; |
| NO_ANSWER | &quot;no_answer&quot; |
| REJECTED | &quot;rejected&quot; |
| ERROR | &quot;error&quot; |



