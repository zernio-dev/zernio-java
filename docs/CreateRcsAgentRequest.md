

# CreateRcsAgentRequest

Send exactly one of brandId or brand.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**brandId** | **String** |  |  [optional] |
|**brand** | [**RcsBrandInput**](RcsBrandInput.md) |  |  [optional] |
|**displayName** | **String** | Shown as the sender name. |  |
|**useCase** | [**UseCaseEnum**](#UseCaseEnum) |  |  |
|**profile** | [**RcsAgentProfile**](RcsAgentProfile.md) |  |  |
|**smsFallbackFrom** | **String** | One of your SMS-enabled numbers. Phones without RCS get the message as SMS from it. |  [optional] |



## Enum: UseCaseEnum

| Name | Value |
|---- | -----|
| MULTI_USE | &quot;MULTI_USE&quot; |
| PROMOTIONAL | &quot;PROMOTIONAL&quot; |
| TRANSACTIONAL | &quot;TRANSACTIONAL&quot; |
| OTP | &quot;OTP&quot; |



