

# WebhookPayloadMessageMetadataUnsupported

WhatsApp only. Meta's own reason this message has no renderable body. Present when Meta attached an error to the inbound payload; in practice the `unsupported`, `errors` and `unknown` types (code 131051: message type currently not supported). `text` on those messages is the fixed `[Unsupported message]` placeholder.  Also present with code 131052 when Meta could not download media the sender attached, except on numbers also using the WhatsApp Business app. The file is not available, so the sender has to send it again. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Meta&#39;s numeric error code (e.g. 131051). |  [optional] |
|**title** | **String** | Meta&#39;s short error title. |  [optional] |
|**details** | **String** | Meta&#39;s human-readable error detail string. |  [optional] |
|**type** | **String** | Meta&#39;s name for the content WhatsApp could not deliver, e.g. view_once, poll_creation, group_invite, edit. Absent when Meta sends none. |  [optional] |



