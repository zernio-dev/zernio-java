

# WebhookPayloadMessageSentMetadataUnsupported

WhatsApp only. Meta's own reason this message has no renderable body. Present on Coexistence echoes of a message sent from the WhatsApp Business app that Meta could not render (for example an album, code 131051: message type currently not supported). Absent otherwise. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Meta&#39;s numeric error code (e.g. 131051). |  [optional] |
|**title** | **String** | Meta&#39;s short error title. |  [optional] |
|**details** | **String** | Meta&#39;s human-readable error detail string. |  [optional] |
|**type** | **String** | Meta&#39;s name for the content WhatsApp could not deliver, e.g. unknown or album. Absent when Meta sends none. |  [optional] |



