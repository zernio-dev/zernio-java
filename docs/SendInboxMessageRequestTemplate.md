

# SendInboxMessageRequestTemplate

Platform-dependent template payload. Ignored on Telegram.  Instagram / Facebook: a generic template (carousel). Set `type: generic` and provide up to 10 `elements`, each with a `title` (required) and optional `subtitle`, `imageUrl`, and `buttons`.  WhatsApp: sends an approved WhatsApp template message, the only message type WhatsApp accepts when the 24-hour customer-service window is closed. Provide exactly one element carrying the template reference: `{ \"elements\": [{ \"name\": \"order_update\", \"language\": \"en_US\", \"components\": [...] }] }` (`type` is ignored on WhatsApp). `components` is optional and is forwarded unchanged as the `template.components` array of Meta's Cloud API send payload; use it to fill body/header variables and button parameters, e.g. `[{ \"type\": \"body\", \"parameters\": [{ \"type\": \"text\", \"text\": \"John\" }] }]`. Templates with media headers (image, video, document) must include the header component with its media link here at send time. To send a template to a phone number with no existing conversation, or to have media headers filled in automatically from the template definition, use the create-conversation endpoint (POST /v1/inbox/conversations) instead. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Template type. Required for Instagram/Facebook generic templates; ignored on WhatsApp. |  [optional] |
|**elements** | [**List&lt;SendInboxMessageRequestTemplateElementsInner&gt;**](SendInboxMessageRequestTemplateElementsInner.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GENERIC | &quot;generic&quot; |



