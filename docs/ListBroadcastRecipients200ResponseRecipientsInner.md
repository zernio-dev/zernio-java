

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
|**errorCode** | **Integer** | Meta WhatsApp error code (e.g. 131049 for antispam, 131021 for invalid phone, 131026 for re-engagement required). Only populated for status&#x3D;failed. |  [optional] |
|**errorExplanation** | **String** | Plain-language translation of errorCode (e.g. for 131026, that the recipient has likely opted out of marketing messages). Null for unmapped codes; fall back to error. |  [optional] |
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



