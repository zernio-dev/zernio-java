

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
|**templateParams** | **List&lt;String&gt;** | WhatsApp only. Template variable values as one flat array, in the order the variables appear across the whole template: text-header variables first, then body variables, then one value per dynamic URL button (in button order). Works with positional placeholders ({{1}}, {{2}}, ...) and with named placeholders ({{name}}, {{company}} - how Meta Business Manager creates templates), where values fill the named slots in order of appearance. Example - a body with {{1}}, {{2}} plus a URL button https://example.com/{{1}} takes three values: [body1, body2, buttonSuffix]. Media headers (image, video, document) are filled automatically from the approved template and take no value here. |  [optional] |



