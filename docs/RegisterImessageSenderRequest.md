

# RegisterImessageSenderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Profile to attach the sender to |  |
|**sender** | **String** | The provider-provisioned sender handle: a phone number in international format (e.g. +18305551234) or an email address |  |
|**displayName** | **String** |  |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | Delivery provider. Defaults to the platform default. |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| LOOPMESSAGE | &quot;loopmessage&quot; |



