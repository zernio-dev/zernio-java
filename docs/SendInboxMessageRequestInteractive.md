

# SendInboxMessageRequestInteractive

WhatsApp-only. Rich interactive payload for list messages, CTA URL buttons, Flow prompts, and location requests. When set, takes priority over `buttons` and `quickReplies`. The shape mirrors Meta's Cloud API `interactive` object verbatim, so any payload that works against Meta directly will also work here.  Use `buttons` / `quickReplies` for simple button replies (WhatsApp's `interactive.type: \"button\"`) — the abstraction caps at 3 buttons and handles the auto-conversion for you. Use this field only for `list`, `cta_url`, `flow`, or `location_request_message` messages.  For `location_request_message`, `action` may be omitted (we default it to `{ \"name\": \"send_location\" }`). WhatsApp renders a localized \"Send location\" button; the user's reply arrives as a regular location message in the conversation.  Tap events come back via the `message.received` webhook with `metadata.interactiveType` set to `list_reply` or `nfm_reply`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Which interactive layout to render. |  |
|**header** | [**SendInboxMessageRequestInteractiveHeader**](SendInboxMessageRequestInteractiveHeader.md) |  |  [optional] |
|**body** | [**SendInboxMessageRequestInteractiveBody**](SendInboxMessageRequestInteractiveBody.md) |  |  |
|**footer** | [**SendInboxMessageRequestInteractiveFooter**](SendInboxMessageRequestInteractiveFooter.md) |  |  [optional] |
|**action** | [**SendInboxMessageRequestInteractiveAction**](SendInboxMessageRequestInteractiveAction.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LIST | &quot;list&quot; |
| CTA_URL | &quot;cta_url&quot; |
| FLOW | &quot;flow&quot; |
| LOCATION_REQUEST_MESSAGE | &quot;location_request_message&quot; |



