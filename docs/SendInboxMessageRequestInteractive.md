

# SendInboxMessageRequestInteractive

WhatsApp-only. Rich interactive payload for list messages, CTA URL buttons, Flow prompts, location requests, voice-call buttons, and commerce messages (single product, product list, catalog, and carousel). When set, takes priority over `buttons` and `quickReplies`. The shape mirrors Meta's Cloud API `interactive` object verbatim, so any payload that works against Meta directly will also work here.  Use `buttons` / `quickReplies` for simple button replies (WhatsApp's `interactive.type: \"button\"`): the abstraction caps at 3 buttons and handles the auto-conversion for you. Use this field only for the types listed in the enum below.  All interactive messages are session messages: they can only be sent inside the 24-hour customer service window opened by the user's last inbound message.  Commerce types (`product`, `product_list`, `catalog_message`, and product carousels) require a Meta catalog connected to the WhatsApp Business Account in Commerce Manager. Media carousels (image/video cards) do not need a catalog.  For `product`, `body` is optional (WhatsApp renders the product card itself) and `header` is not allowed (the product image is the header). For `product_list`, a `header` with `type: \"text\"` is required. For `carousel`, top-level `header`/`footer` are not supported; media goes on each card instead.  For `voice_call`, the message renders WhatsApp's native call button; tapping it starts a voice call to your business number. Requires WhatsApp Business Calling to be enabled on the sending number. The optional `parameters.payload` string is echoed back on the `calls` webhook (as `cta_payload`) for attribution.  For `location_request_message`, `action` may be omitted (we default it to `{ \"name\": \"send_location\" }`). WhatsApp renders a localized \"Send location\" button; the user's reply arrives as a regular location message in the conversation.  For `request_contact_info`, `action` may be omitted (we default it to `{ \"name\": \"request_contact_info\" }`). WhatsApp renders a localized share button that cannot be relabelled, so put the reason for asking in `body.text`: this is a consent prompt, and a bare request converts badly. The reply arrives as an inbound `contacts` message with `metadata.contactsOrigin` set to `contact_request`, and we fold the shared number back into the contact automatically. A `contacts` message with origin `other` is a card the user picked from their address book and is NOT proof of their own number.  For `catalog_message`, `action` may also be omitted (we default it to `{ \"name\": \"catalog_message\" }`).  Tap events come back via the `message.received` webhook with `metadata.interactiveType` set to `list_reply` or `nfm_reply`. Carts submitted from commerce messages arrive as `metadata.order`; product inquiries arrive as `metadata.referredProduct`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Which interactive layout to render. |  |
|**header** | [**SendInboxMessageRequestInteractiveHeader**](SendInboxMessageRequestInteractiveHeader.md) |  |  [optional] |
|**body** | [**SendInboxMessageRequestInteractiveBody**](SendInboxMessageRequestInteractiveBody.md) |  |  [optional] |
|**footer** | [**SendInboxMessageRequestInteractiveFooter**](SendInboxMessageRequestInteractiveFooter.md) |  |  [optional] |
|**action** | [**SendInboxMessageRequestInteractiveAction**](SendInboxMessageRequestInteractiveAction.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LIST | &quot;list&quot; |
| CTA_URL | &quot;cta_url&quot; |
| FLOW | &quot;flow&quot; |
| LOCATION_REQUEST_MESSAGE | &quot;location_request_message&quot; |
| REQUEST_CONTACT_INFO | &quot;request_contact_info&quot; |
| VOICE_CALL | &quot;voice_call&quot; |
| PRODUCT | &quot;product&quot; |
| PRODUCT_LIST | &quot;product_list&quot; |
| CATALOG_MESSAGE | &quot;catalog_message&quot; |
| CAROUSEL | &quot;carousel&quot; |



