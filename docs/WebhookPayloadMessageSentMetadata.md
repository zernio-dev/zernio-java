

# WebhookPayloadMessageSentMetadata

Platform-specific context for the sent message: a quote-reply reference, a WhatsApp location pin, WhatsApp contact cards, the TikTok message type, or outgoing Instagram/Facebook buttons, quick replies and template.  The key is present only when the send carried some context: it is never null and never an empty object. Read it to tell a location or contact-card message from a text one without a GET on the message. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metaInteractive** | **Map&lt;String, Object&gt;** | Instagram/Facebook only. The buttons, quickReplies and/or template this outgoing message carried, as sent (tracked urls included when link tracking wrapped a button). Absent when the send carried none. |  [optional] |
|**location** | [**WebhookPayloadMessageSentMetadataLocation**](WebhookPayloadMessageSentMetadataLocation.md) |  |  [optional] |
|**contacts** | **List&lt;Map&lt;String, Object&gt;&gt;** | WhatsApp only. The contact cards this message carries. The message &#x60;text&#x60; is only the emoji preview (&#x60;👤 &lt;name&gt;&#x60;); the cards live here.  - API sends: the &#x60;contacts&#x60; array exactly as given to the inbox send API (&#x60;name&#x60;, &#x60;phones[].phone&#x60; / &#x60;type&#x60;, &#x60;emails[]&#x60;). - Coexistence echoes of a card shared from the WhatsApp Business app: Meta&#39;s shape (&#x60;phones[].wa_id&#x60;, &#x60;vcard&#x60;).  |  [optional] |
|**quotedMessageId** | **String** | &#x60;platformMessageId&#x60; of the message this send quote-replies to.  - **WhatsApp and Telegram:** present when the reply was sent through Zernio with &#x60;replyTo&#x60; on the inbox send API. A WhatsApp API send fires &#x60;message.sent&#x60; off the delivery status, with the quote reference forwarded from the stored send, so it arrives on the same &#x60;message.sent&#x60; as any WhatsApp send. - **Instagram echoes:** not delivered. Zernio forwards &#x60;reply_to.mid&#x60; whenever Meta puts it on an echo, but on Instagram Meta does not send it, so a reply the operator quoted in the Instagram app arrives with no &#x60;quotedMessageId&#x60;. - **Facebook Messenger:** uses a separate subscription (&#x60;message_echoes&#x60;) that has not been measured. Treat it as unverified, not supported. - **WhatsApp Coexistence echoes:** absent. Meta omits the quote context from &#x60;smb_message_echoes&#x60;, so a reply the operator sent from the WhatsApp Business app has no &#x60;quotedMessageId&#x60; even though WhatsApp shows it as a quote-reply.  Do not read the absence of this field as \&quot;not a reply\&quot;.  |  [optional] |
|**threadTs** | **String** | Slack only. Parent thread ts of the sent message. Pass it back as &#x60;replyTo&#x60; on the inbox send API to keep replying inside the thread.  |  [optional] |
|**tiktokMessageType** | **String** | TikTok only. The message type as TikTok reports it, forwarded verbatim (for example image, video, sticker, share_post, emoji, reaction, template).  Present on every TikTok DM that is not plain text. Those arrive with text empty and, for image, video, share_post, sticker and emoji, an attachment:  - share_post: type share, with the embed url and payload.videoId. - sticker/emoji: type sticker, url signed and expiring.  Absent on image sends made through the Zernio API, which carry the image in attachments.  |  [optional] |



