

# CreateVerificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  |
|**to** | **String** | E.164 phone number. WhatsApp only delivers to a phone number, never to a username. |  |
|**from** | **String** | The number on your account to send from: an SMS-enabled number for &#x60;sms&#x60;, a connected WhatsApp number for &#x60;whatsapp&#x60;. Defaults to your only number on that channel. |  [optional] |
|**brandName** | **String** | Your app or business name, rendered in the SMS message. Defaults to your account name. Not shown on WhatsApp, where Meta fixes the message and shows your WhatsApp display name. Letters, numbers, and basic punctuation only. |  [optional] |
|**codeLength** | **Integer** |  |  [optional] |
|**ttlMinutes** | **Integer** |  |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |
| WHATSAPP | &quot;whatsapp&quot; |



