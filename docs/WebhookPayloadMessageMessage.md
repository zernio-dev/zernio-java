

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
|**sentVia** | [**SentViaEnum**](#SentViaEnum) | Which Zernio surface produced the message. Always present and always &#x60;null&#x60; on this event, since nobody on our side produced an inbound message; it is only informative on &#x60;message.sent&#x60;, which documents the vocabulary.  |  [optional] |



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



## Enum: SentViaEnum

| Name | Value |
|---- | -----|
| HUMAN | &quot;human&quot; |
| API | &quot;api&quot; |
| BROADCAST | &quot;broadcast&quot; |
| SEQUENCE | &quot;sequence&quot; |
| WORKFLOW | &quot;workflow&quot; |
| COMMENT_AUTOMATION | &quot;comment_automation&quot; |
| BULK_API | &quot;bulk-api&quot; |



