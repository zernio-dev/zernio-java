

# GetWhatsAppCalling200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumber** | **String** |  |  [optional] |
|**callingEnabled** | **Boolean** |  |  [optional] |
|**callDeepLink** | **String** | Public calling deep link (https://wa.me/call/&lt;number&gt;). Null while calling is disabled. |  [optional] |
|**forwardTo** | **String** | tel:+E164 / sip:... / wss://... destination |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**sipAuthUsername** | **String** |  |  [optional] |
|**sipAuthPasswordConfigured** | **Boolean** | True when a SIP digest password is stored. The plaintext is never returned. |  [optional] |
|**callIconCountries** | **List&lt;String&gt;** |  |  [optional] |
|**outboundDisabled** | **Boolean** | True when the number&#39;s country blocks business-initiated (outbound) WhatsApp calling; inbound still works. |  [optional] |
|**callerIdMode** | [**CallerIdModeEnum**](#CallerIdModeEnum) | Caller ID the forward-leg callee sees on tel: forwards. business &#x3D; this WhatsApp number; platform &#x3D; a Zernio number (used when the number was brought by the customer and its caller ID is not verified for PSTN origination). |  [optional] |
|**callerIdVerified** | **Boolean** | True once the number completed caller-ID verification, making tel: forwards display the business number itself. |  [optional] |



## Enum: CallerIdModeEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| PLATFORM | &quot;platform&quot; |



