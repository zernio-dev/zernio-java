

# WebhookPayloadMessageSentMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Internal message ID |  |
|**conversationId** | **String** | Internal conversation ID |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Every platform whose outgoing messages Zernio observes. sms is absent on purpose: its carrier receipts update delivery status and never raise message.sent. |  |
|**platformMessageId** | **String** | Platform&#39;s message ID |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**text** | **String** | Message text content |  |
|**attachments** | [**List&lt;WebhookPayloadMessageSentMessageAttachmentsInner&gt;**](WebhookPayloadMessageSentMessageAttachmentsInner.md) |  |  |
|**sender** | [**WebhookPayloadMessageSentMessageSender**](WebhookPayloadMessageSentMessageSender.md) |  |  |
|**sentAt** | **OffsetDateTime** | When the message was sent, as reported by the platform and passed through unmodified. Full ISO 8601 date-time: Instagram and Facebook carry millisecond precision, while some platforms (for example WhatsApp and Telegram) report whole seconds. Use this field as the chronological ordering key. If two messages share the same value, fetch the conversation messages with sortOrder&#x3D;desc for the deterministic order. |  |
|**isRead** | **Boolean** |  |  |
|**source** | [**SourceEnum**](#SourceEnum) | WhatsApp send origin. whatsapp_business_app when sent from the WhatsApp Business phone app on a Coexistence number; cloud_api when sent through Zernio (dashboard, API, or broadcasts). Absent on non-WhatsApp platforms. Says where WhatsApp saw the send come from, not which Zernio surface produced it: read sentVia for that. |  [optional] |
|**sentVia** | [**SentViaEnum**](#SentViaEnum) | Which Zernio surface produced this message: &#x60;human&#x60; (an operator in the Zernio inbox), &#x60;api&#x60; (a call to this API), &#x60;broadcast&#x60;, &#x60;sequence&#x60;, &#x60;workflow&#x60;, &#x60;comment_automation&#x60;, or &#x60;bulk-api&#x60; (POST /v1/whatsapp/bulk). Same vocabulary as the &#x60;source&#x60; filter on the inbox analytics endpoints, and the same value a later GET on this message returns.  Always present, and &#x60;null&#x60; whenever the lineage is unknown: a message sent from the platform&#39;s own app, and every message stored before this field shipped (2026-08). Existing messages are NOT backfilled, so treat &#x60;null&#x60; as \&quot;unknown\&quot;, never as \&quot;sent by a human\&quot;.  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TELEGRAM | &quot;telegram&quot; |
| WHATSAPP | &quot;whatsapp&quot; |
| TWITTER | &quot;twitter&quot; |
| REDDIT | &quot;reddit&quot; |
| BLUESKY | &quot;bluesky&quot; |
| SLACK | &quot;slack&quot; |



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



