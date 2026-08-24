

# WebhookPayloadMessageMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Internal message ID |  |
|**conversationId** | **String** | Internal conversation ID |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**platformMessageId** | **String** | Platform&#39;s message ID |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**text** | **String** | Message text content |  |
|**attachments** | [**List&lt;WebhookPayloadMessageMessageAttachmentsInner&gt;**](WebhookPayloadMessageMessageAttachmentsInner.md) |  |  |
|**sender** | [**WebhookPayloadMessageMessageSender**](WebhookPayloadMessageMessageSender.md) |  |  |
|**sentAt** | **OffsetDateTime** | When the message was sent, as reported by the platform and passed through unmodified. Full ISO 8601 date-time: Instagram and Facebook carry millisecond precision, while some platforms (for example WhatsApp and Telegram) report whole seconds. Use this field as the chronological ordering key. If two messages share the same value, fetch the conversation messages with sortOrder&#x3D;desc for the deterministic order. |  |
|**isRead** | **Boolean** |  |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TELEGRAM | &quot;telegram&quot; |
| WHATSAPP | &quot;whatsapp&quot; |
| SMS | &quot;sms&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INCOMING | &quot;incoming&quot; |
| OUTGOING | &quot;outgoing&quot; |



