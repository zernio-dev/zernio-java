

# CreateInboxConversationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The social account ID to send from |  |
|**participantId** | **String** | Recipient identifier. For X this is the numeric user ID; for WhatsApp and SMS, the recipient phone number in international format (digits, country code included); for Slack, the workspace member id (e.g. U01ABCDEF). Provide either this or participantUsername. |  [optional] |
|**participantUsername** | **String** | Recipient handle/username — an X or Bluesky handle (with or without @) or a Reddit username (with or without u/). Resolved via lookup. Provide either this or participantId. |  [optional] |
|**message** | **String** | Text content of the message. At least one of message, attachment, or (for WhatsApp) templateName is required. Required when category is set (a Direct Send utility message is a text message). |  [optional] |
|**skipDmCheck** | **Boolean** | X/Twitter only. Skip the receives_your_dm eligibility check before sending. Use if you have already verified the recipient accepts DMs. |  [optional] |
|**templateName** | **String** | WhatsApp only. Name of the approved template to start the conversation with. Required for WhatsApp unless category is used instead (Direct Send). Cannot be combined with category. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | WhatsApp only (Meta Direct Send). Combined with message and without templateName, starts the conversation with a business-initiated UTILITY message and no pre-approved template; Meta matches or auto-creates a template asynchronously. The WhatsApp Business Account must be eligible for Direct Send, otherwise the send fails with an error telling you to use an approved message template instead. Cannot be combined with templateName (templates are already categorized at creation). Utility messages only; marketing content is not allowed under this category. Accepted on the JSON body only, not on multipart requests. |  [optional] |
|**linkPreview** | **Boolean** | WhatsApp only. Set false to send the Direct Send (category: &#39;utility&#39;) text message without a link-preview thumbnail for the first URL in the text. Defaults to true, which is how every WhatsApp text has been sent to date. Does not apply to template sends. Accepted on the JSON body only, not on multipart requests. |  [optional] |
|**templateLanguage** | **String** | WhatsApp only. Template language code (e.g. en_US). |  [optional] |
|**templateParams** | **List&lt;String&gt;** | WhatsApp only. Template variable values as one flat array, in the order the variables appear across the whole template: text-header variables first, then body variables, then one value per dynamic URL button (in button order). Works with positional placeholders ({{1}}, {{2}}, ...) and with named placeholders ({{name}}, {{company}} - how Meta Business Manager creates templates), where values fill the named slots in order of appearance. Example - a body with {{1}}, {{2}} plus a URL button https://example.com/{{1}} takes three values: [body1, body2, buttonSuffix]. Media headers (image, video, document) are filled automatically from the approved template and take no value here (use headerMedia to override the header asset per send). Buttons that are not dynamic-URL buttons (copy-code, flow) take no value here either; use templateButtonParams. |  [optional] |
|**templateButtonParams** | [**List&lt;CreateInboxConversationRequestTemplateButtonParamsInner&gt;**](CreateInboxConversationRequestTemplateButtonParamsInner.md) | WhatsApp only. Values for template buttons that carry one at send time, each addressed by the button&#39;s position in the approved template. This is the only way to send a copy-code button&#39;s payload (a Pix payment code, a coupon) or a flow token, because templateParams is a flat array of text variables and covers dynamic URL buttons only. Supplying a button here overrides whatever templateParams would have derived for that same index, so the send never carries one button twice; repeating an index within this array is rejected with 400. Each index must name a button of the matching kind on the approved template, which is also checked before the send and returns 400 (INVALID_TEMPLATE_BUTTON_PARAM) rather than a Meta rejection. |  [optional] |
|**headerMedia** | [**CreateInboxConversationRequestHeaderMedia**](CreateInboxConversationRequestHeaderMedia.md) |  |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| UTILITY | &quot;utility&quot; |



