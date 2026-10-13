

# CtwaAdRequestBodyCreativesInnerWelcomeMessage

Custom chat welcome message for this entry: `text` plus exactly one of `prefillText` or `quickReplies` (400 otherwise). Same shape as the top-level `welcomeMessage` of the single-creative shape.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**text** | **String** | Greeting shown when the chat opens. Replaces Meta&#39;s default. |  |
|**prefillText** | **String** | Message put into the user&#39;s text input, ready to send. Replaces Meta&#39;s default. Exactly one of prefillText or quickReplies. |  [optional] |
|**quickReplies** | [**List&lt;CtwaAdRequestBodyWelcomeMessageQuickRepliesInner&gt;**](CtwaAdRequestBodyWelcomeMessageQuickRepliesInner.md) | Tappable chips under the greeting instead of a prefilled message. Exactly one of prefillText or quickReplies. |  [optional] |



