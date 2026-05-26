

# CreateInboxConversationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The social account ID to send from |  |
|**participantId** | **String** | Recipient identifier. For X this is the numeric user ID; for WhatsApp, the recipient phone number in international format (digits, country code included). Provide either this or participantUsername. |  [optional] |
|**participantUsername** | **String** | Recipient handle/username — an X or Bluesky handle (with or without @) or a Reddit username (with or without u/). Resolved via lookup. Provide either this or participantId. |  [optional] |
|**message** | **String** | Text content of the message. At least one of message, attachment, or (for WhatsApp) templateName is required. |  [optional] |
|**skipDmCheck** | **Boolean** | X/Twitter only. Skip the receives_your_dm eligibility check before sending. Use if you have already verified the recipient accepts DMs. |  [optional] |
|**templateName** | **String** | WhatsApp only. Name of the approved template to start the conversation with (required for WhatsApp). |  [optional] |
|**templateLanguage** | **String** | WhatsApp only. Template language code (e.g. en_US). |  [optional] |
|**templateParams** | **List&lt;String&gt;** | WhatsApp only. Body variable values, in order, substituted into the template body ({{1}}, {{2}}, ...). |  [optional] |



