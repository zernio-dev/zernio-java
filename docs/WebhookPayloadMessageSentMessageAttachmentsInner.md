

# WebhookPayloadMessageSentMessageAttachmentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | Attachment type (image, video, file, sticker, audio) |  |
|**url** | **String** | Where to fetch the attachment. For outgoing messages this is the media URL as sent, so for WhatsApp it is the URL you supplied when publishing (WhatsApp sends media by link), not a Zernio endpoint, and it needs no Zernio credentials. Contrast the inbound direction: &#x60;message.received&#x60; attachment URLs on WhatsApp point at the authenticated &#x60;GET /v1/whatsapp/media/{mediaId}&#x60;.  |  |
|**payload** | **Object** | Additional attachment metadata |  [optional] |



