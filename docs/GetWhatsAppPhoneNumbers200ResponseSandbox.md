

# GetWhatsAppPhoneNumbers200ResponseSandbox

The shared WhatsApp sandbox (one Zernio-owned number, all users test against it). Present when the sandbox is configured; null otherwise. The `accountId` lets you address the sandbox in compose endpoints. `template` is the only template a sandbox send is allowed to use. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumber** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**template** | [**GetWhatsAppPhoneNumbers200ResponseSandboxTemplate**](GetWhatsAppPhoneNumbers200ResponseSandboxTemplate.md) |  |  [optional] |
|**isSandbox** | [**IsSandboxEnum**](#IsSandboxEnum) |  |  [optional] |



## Enum: IsSandboxEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |



