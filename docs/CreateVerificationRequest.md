

# CreateVerificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) | SMS-only for now. |  |
|**to** | **String** | E.164 phone number. |  |
|**from** | **String** | The SMS-enabled number on your account to send from. Defaults to your only SMS number. |  [optional] |
|**brandName** | **String** | Your app or business name, rendered in the message. Defaults to your account name. Letters, numbers, and basic punctuation only. |  [optional] |
|**codeLength** | **Integer** |  |  [optional] |
|**ttlMinutes** | **Integer** |  |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |



