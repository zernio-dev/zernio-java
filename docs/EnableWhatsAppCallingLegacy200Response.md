

# EnableWhatsAppCallingLegacy200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**callingEnabled** | **Boolean** |  |  [optional] |
|**sipHostname** | **String** |  |  [optional] |
|**forwardTo** | **String** |  |  [optional] |
|**callerIdMode** | [**CallerIdModeEnum**](#CallerIdModeEnum) | Caller ID the forward-leg callee sees on tel: forwards. business &#x3D; this WhatsApp number; platform &#x3D; a Zernio number (customer-brought number without verified caller ID). |  [optional] |



## Enum: CallerIdModeEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| PLATFORM | &quot;platform&quot; |



