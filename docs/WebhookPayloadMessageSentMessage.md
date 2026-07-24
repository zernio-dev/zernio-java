

# WebhookPayloadMessageSentMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Internal message ID |  |
|**conversationId** | **String** | Internal conversation ID |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**platformMessageId** | **String** | Platform&#39;s message ID |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**text** | **String** | Message text content |  |
|**attachments** | [**List&lt;WebhookPayloadMessageSentMessageAttachmentsInner&gt;**](WebhookPayloadMessageSentMessageAttachmentsInner.md) |  |  |
|**sender** | [**WebhookPayloadMessageSentMessageSender**](WebhookPayloadMessageSentMessageSender.md) |  |  |
|**sentAt** | **OffsetDateTime** |  |  |
|**isRead** | **Boolean** |  |  |
|**source** | [**SourceEnum**](#SourceEnum) | WhatsApp send origin. whatsapp_business_app when sent from the WhatsApp Business phone app on a Coexistence number; cloud_api when sent through Zernio (dashboard, API, or broadcasts). Absent on non-WhatsApp platforms. This is not the inbox metadata.source lineage field. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TELEGRAM | &quot;telegram&quot; |
| WHATSAPP | &quot;whatsapp&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INCOMING | &quot;incoming&quot; |
| OUTGOING | &quot;outgoing&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| WHATSAPP_BUSINESS_APP | &quot;whatsapp_business_app&quot; |
| CLOUD_API | &quot;cloud_api&quot; |



