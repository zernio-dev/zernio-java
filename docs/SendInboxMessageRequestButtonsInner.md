

# SendInboxMessageRequestButtonsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Button type. phone is Facebook only. Ignored on WhatsApp (buttons always render as reply buttons). |  |
|**title** | **String** | Button label (max 20 chars) |  |
|**url** | **String** | URL for url-type buttons (Facebook/Instagram only) |  [optional] |
|**payload** | **String** | Payload for postback-type buttons. On WhatsApp, this is the reply ID returned on the message.received webhook when the button is tapped. |  [optional] |
|**phone** | **String** | Phone number for phone-type buttons (Facebook only) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| URL | &quot;url&quot; |
| POSTBACK | &quot;postback&quot; |
| PHONE | &quot;phone&quot; |



