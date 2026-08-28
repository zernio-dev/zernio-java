

# GetInboxConversationMessages200ResponseMessagesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**conversationId** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**senderId** | **String** |  |  [optional] |
|**senderName** | **String** |  |  [optional] |
|**senderVerifiedType** | [**SenderVerifiedTypeEnum**](#SenderVerifiedTypeEnum) | X/Twitter verified badge type. Only present for Twitter/X messages. |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**attachments** | [**List&lt;GetInboxConversationMessages200ResponseMessagesInnerAttachmentsInner&gt;**](GetInboxConversationMessages200ResponseMessagesInnerAttachmentsInner.md) |  |  [optional] |
|**subject** | **String** | Reddit message subject |  [optional] |
|**storyReply** | **Boolean** | Instagram story reply |  [optional] |
|**isStoryMention** | **Boolean** | Instagram story mention |  [optional] |
|**isEdited** | **Boolean** | True if the sender has edited this message at least once. |  [optional] |
|**editedAt** | **OffsetDateTime** | When the most recent edit happened. |  [optional] |
|**editCount** | **Integer** | Total number of edits applied. |  [optional] |
|**editHistory** | [**List&lt;InboxMessageEditHistoryEntry&gt;**](InboxMessageEditHistoryEntry.md) | Every prior version of the message, oldest first. |  [optional] |
|**isDeleted** | **Boolean** | True if the sender has deleted (unsent) this message. The original message and attachments fields remain populated. |  [optional] |
|**deletedAt** | **OffsetDateTime** |  |  [optional] |
|**deliveryStatus** | [**DeliveryStatusEnum**](#DeliveryStatusEnum) | Lifecycle status for outgoing messages. Not all platforms emit every state (see webhook support matrix). |  [optional] |
|**deliveredAt** | **OffsetDateTime** |  |  [optional] |
|**readAt** | **OffsetDateTime** |  |  [optional] |
|**sentAt** | **OffsetDateTime** | Original send time for outgoing messages (used for Messenger watermark queries). |  [optional] |
|**deliveryError** | [**GetInboxConversationMessages200ResponseMessagesInnerDeliveryError**](GetInboxConversationMessages200ResponseMessagesInnerDeliveryError.md) |  |  [optional] |
|**reactions** | [**List&lt;GetInboxConversationMessages200ResponseMessagesInnerReactionsInner&gt;**](GetInboxConversationMessages200ResponseMessagesInnerReactionsInner.md) | Emoji reactions on this message (WhatsApp / Telegram). At most one per party in a 1:1 thread. |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | Platform-specific extras. Free-form, but commonly includes: &#x60;quotedMessageId&#x60; (platformMessageId this message replies to), &#x60;waInteractive&#x60; (a compact descriptor of WhatsApp interactive content sent: buttons / list / cta_url / flow / location_request), and for inbound interactive taps &#x60;interactiveType&#x60; / &#x60;interactiveId&#x60;. It can also carry &#x60;source&#x60; (&#x60;whatsapp_business_app&#x60; / &#x60;coexistence_history&#x60; on a WhatsApp Coexistence number, &#x60;bulk-api&#x60; on a POST /v1/whatsapp/bulk send), which is where the message reached us from rather than who produced it: read &#x60;sentVia&#x60; for that.  |  [optional] |
|**sentVia** | [**SentViaEnum**](#SentViaEnum) | Which Zernio surface produced this outgoing message: &#x60;human&#x60; (an operator in the Zernio inbox), &#x60;api&#x60; (a call to this API), &#x60;broadcast&#x60;, &#x60;sequence&#x60;, &#x60;workflow&#x60;, &#x60;comment_automation&#x60;, or &#x60;bulk-api&#x60; (POST /v1/whatsapp/bulk). Same vocabulary as the &#x60;source&#x60; filter on the inbox analytics endpoints.  Always present, and &#x60;null&#x60; whenever the lineage is unknown: every incoming message, any outgoing message sent from the platform&#39;s own app, and every message stored before this field shipped (2026-08). Existing messages are NOT backfilled, so treat &#x60;null&#x60; as \&quot;unknown\&quot;, never as \&quot;sent by a human\&quot;.  |  [optional] |



## Enum: SenderVerifiedTypeEnum

| Name | Value |
|---- | -----|
| BLUE | &quot;blue&quot; |
| GOVERNMENT | &quot;government&quot; |
| BUSINESS | &quot;business&quot; |
| NONE | &quot;none&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INCOMING | &quot;incoming&quot; |
| OUTGOING | &quot;outgoing&quot; |



## Enum: DeliveryStatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| DELIVERED | &quot;delivered&quot; |
| READ | &quot;read&quot; |
| FAILED | &quot;failed&quot; |
| DELETED | &quot;deleted&quot; |



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



