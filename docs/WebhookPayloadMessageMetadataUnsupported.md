

# WebhookPayloadMessageMetadataUnsupported

WhatsApp only. Meta's own reason this message has no renderable body. Present when Meta attached an error to the inbound payload; in practice the `unsupported`, `errors` and `unknown` types (code 131051: message type currently not supported). `text` on those messages is the fixed `[Unsupported message]` placeholder. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Meta&#39;s numeric error code (e.g. 131051). |  [optional] |
|**title** | **String** | Meta&#39;s short error title. |  [optional] |
|**details** | **String** | Meta&#39;s human-readable error detail string. |  [optional] |



