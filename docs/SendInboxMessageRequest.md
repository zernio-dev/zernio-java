

# SendInboxMessageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Social account ID |  |
|**message** | **String** | Message text |  [optional] |
|**attachmentUrl** | **String** | URL of the attachment to send (image, video, audio, or file). The URL must be publicly accessible. For binary file uploads, use multipart/form-data instead. |  [optional] |
|**attachmentType** | [**AttachmentTypeEnum**](#AttachmentTypeEnum) | Type of attachment. Defaults to file if not specified. |  [optional] |
|**attachmentName** | **String** | WhatsApp only. Display name for a document sent via attachmentUrl with attachmentType: file (e.g. \&quot;Report.pdf\&quot;). Maps to the recipient&#39;s file name; without it WhatsApp derives the name from the URL and shows \&quot;Untitled\&quot;. Ignored for image/video/audio and for binary uploads (which use the uploaded file&#39;s name). |  [optional] |
|**voiceNote** | **Boolean** | WhatsApp only. When &#x60;true&#x60; on an audio attachment, the message is sent as a voice message (PTT) — the recipient sees the waveform + voice-note UI instead of a basic audio attachment. The audio file MUST be &#x60;.ogg&#x60; encoded with the OPUS codec (mono) per Meta&#39;s voice-message contract; other formats are rejected by WhatsApp. Ignored for non-audio attachments.  |  [optional] |
|**quickReplies** | [**List&lt;SendInboxMessageRequestQuickRepliesInner&gt;**](SendInboxMessageRequestQuickRepliesInner.md) | Quick reply buttons. Mutually exclusive with buttons. Max 13 items. |  [optional] |
|**buttons** | [**List&lt;SendInboxMessageRequestButtonsInner&gt;**](SendInboxMessageRequestButtonsInner.md) | Action buttons. Mutually exclusive with quickReplies. Max 3 items.  WhatsApp: buttons always render as interactive reply buttons. Only &#x60;title&#x60; and &#x60;payload&#x60; are used — &#x60;type&#x60;, &#x60;url&#x60;, and &#x60;phone&#x60; are ignored (WhatsApp has no URL/phone button in this field; use the &#x60;interactive&#x60; field with &#x60;type: cta_url&#x60; for a link button). &#x60;payload&#x60; becomes the button reply ID delivered on the &#x60;message.received&#x60; webhook when the user taps. To send a simple reply-button message, provide &#x60;title&#x60; + &#x60;payload&#x60; and set &#x60;type: postback&#x60;, e.g. &#x60;{ \&quot;type\&quot;: \&quot;postback\&quot;, \&quot;title\&quot;: \&quot;Yes\&quot;, \&quot;payload\&quot;: \&quot;yes\&quot; }&#x60;.  |  [optional] |
|**template** | [**SendInboxMessageRequestTemplate**](SendInboxMessageRequestTemplate.md) |  |  [optional] |
|**interactive** | [**SendInboxMessageRequestInteractive**](SendInboxMessageRequestInteractive.md) |  |  [optional] |
|**replyMarkup** | [**SendInboxMessageRequestReplyMarkup**](SendInboxMessageRequestReplyMarkup.md) |  |  [optional] |
|**messagingType** | [**MessagingTypeEnum**](#MessagingTypeEnum) | Facebook messaging type. Required when using messageTag. |  [optional] |
|**messageTag** | [**MessageTagEnum**](#MessageTagEnum) | Facebook message tag for messaging outside 24h window. Requires messagingType MESSAGE_TAG. Instagram only supports HUMAN_AGENT. |  [optional] |
|**replyTo** | **String** | Platform message ID to quote-reply to. For WhatsApp, pass the wamid (available in message.platformMessageId from webhooks). For Telegram, pass the Telegram message ID. |  [optional] |
|**location** | [**SendInboxMessageRequestLocation**](SendInboxMessageRequestLocation.md) |  |  [optional] |
|**contacts** | [**List&lt;SendInboxMessageRequestContactsInner&gt;**](SendInboxMessageRequestContactsInner.md) | WhatsApp-only. Send one or more contact cards. |  [optional] |



## Enum: AttachmentTypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| AUDIO | &quot;audio&quot; |
| FILE | &quot;file&quot; |



## Enum: MessagingTypeEnum

| Name | Value |
|---- | -----|
| RESPONSE | &quot;RESPONSE&quot; |
| UPDATE | &quot;UPDATE&quot; |
| MESSAGE_TAG | &quot;MESSAGE_TAG&quot; |



## Enum: MessageTagEnum

| Name | Value |
|---- | -----|
| CONFIRMED_EVENT_UPDATE | &quot;CONFIRMED_EVENT_UPDATE&quot; |
| POST_PURCHASE_UPDATE | &quot;POST_PURCHASE_UPDATE&quot; |
| ACCOUNT_UPDATE | &quot;ACCOUNT_UPDATE&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |



