

# CtwaAdRequestBodyWelcomeMessage

Custom chat welcome message (Meta's `page_welcome_message`, \"Mensaje de bienvenida\" / \"Mensaje predefinido\" in Ads Manager). Single-creative shape only; for `creatives[]` set it per entry. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**text** | **String** | Greeting shown when the chat opens. Replaces Meta&#39;s default (\&quot;Hi! Can we help you?\&quot;). |  |
|**prefillText** | **String** | Message put into the user&#39;s text input, ready to send. Replaces Meta&#39;s default (\&quot;Hi! I want more info.\&quot;). Lets one ad steer the opening message toward what it promotes (e.g. a specific product). Exactly one of prefillText or quickReplies. |  [optional] |
|**quickReplies** | [**List&lt;CtwaAdRequestBodyWelcomeMessageQuickRepliesInner&gt;**](CtwaAdRequestBodyWelcomeMessageQuickRepliesInner.md) | Tappable chips under the greeting instead of a prefilled message. Exactly one of prefillText or quickReplies. Put your own campaign or ad key in each payload: the tap arrives on the messages webhook with that payload even where Meta delivers no ad referral (Pages owned by an EU business under the Europe/Japan Messenger restrictions).  |  [optional] |



