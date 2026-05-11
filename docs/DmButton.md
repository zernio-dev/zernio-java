

# DmButton

A single inline button rendered inside an auto-DM via Meta's button_template. Up to 3 buttons per automation. `url` and `postback` work on Instagram and Facebook; `phone` is Facebook-only. When buttons are set, `dmMessage` becomes the button_template text and must be 640 characters or less. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**title** | **String** | Button label (20 chars max) |  |
|**url** | **URI** | Target URL (required when type is url) |  [optional] |
|**payload** | **String** | Postback payload delivered via the messaging_postbacks webhook (required when type is postback) |  [optional] |
|**phone** | **String** | Phone number, e.g. +14155551234 (required when type is phone; Facebook only) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| URL | &quot;url&quot; |
| POSTBACK | &quot;postback&quot; |
| PHONE | &quot;phone&quot; |



