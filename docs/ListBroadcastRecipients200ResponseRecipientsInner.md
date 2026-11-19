

# ListBroadcastRecipients200ResponseRecipientsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**contactId** | **String** |  |  [optional] |
|**channelId** | **String** |  |  [optional] |
|**platformIdentifier** | **String** |  |  [optional] |
|**contactName** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**messageId** | **String** |  |  [optional] |
|**error** | **String** |  |  [optional] |
|**errorCode** | **Integer** | Meta WhatsApp error code (e.g. 131049 for a per-user marketing limit, 131021 for a recipient that is the sending number, 131026 for an undeliverable message). Only populated for status&#x3D;failed. |  [optional] |
|**errorExplanation** | **String** | Plain-language translation of errorCode (e.g. for 131026, that the recipient has likely opted out of marketing messages). Null for unmapped codes; fall back to error. |  [optional] |
|**errorTraceId** | **String** | Meta trace id (fbtrace_id) for the failed send. Quote this when escalating to Meta Direct Support. Only populated for status&#x3D;failed on Meta platforms. |  [optional] |
|**sentAt** | **OffsetDateTime** |  |  [optional] |
|**deliveredAt** | **OffsetDateTime** |  |  [optional] |
|**readAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| SENT | &quot;sent&quot; |
| DELIVERED | &quot;delivered&quot; |
| READ | &quot;read&quot; |
| FAILED | &quot;failed&quot; |



