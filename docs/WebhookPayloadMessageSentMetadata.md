

# WebhookPayloadMessageSentMetadata

Platform-specific context for the sent message. The key is present only when the send carried some context, and absent otherwise: it is never null and never an empty object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**quotedMessageId** | **String** | platformMessageId of the message this send is a quote-reply to. Set when the reply was sent through Zernio with &#x60;replyTo&#x60; on the inbox send API (WhatsApp and Telegram), and when the operator replied from the native WhatsApp Business, Instagram or Messenger app. WhatsApp API sends carry it on the event fired from the delivery status, so it arrives on the same &#x60;message.sent&#x60; as any other WhatsApp send.  |  [optional] |
|**threadTs** | **String** | Slack only. Parent thread ts of the sent message. Pass it back as &#x60;replyTo&#x60; on the inbox send API to keep replying inside the thread.  |  [optional] |



