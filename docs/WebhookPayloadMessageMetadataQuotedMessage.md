

# WebhookPayloadMessageMetadataQuotedMessage

Zernio's own ids for the message this one quote-replies to. Present only when that message is stored; WhatsApp only today.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageId** | **String** | Internal id of the stored quoted message. |  [optional] |
|**platformMessageId** | **String** | The STORED message&#39;s platform id (what message.sent and list-messages return). Can differ from quotedMessageId, because Meta renders one message under a different wamid per perspective. |  [optional] |



