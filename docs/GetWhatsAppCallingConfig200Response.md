

# GetWhatsAppCallingConfig200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumberDocId** | **String** | Phone number record ID (use on /v1/phone-numbers/{id}/whatsapp/calling) |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**callingEnabled** | **Boolean** |  |  [optional] |
|**callDeepLink** | **String** | Public calling deep link (https://wa.me/call/&lt;number&gt;). Tapping it on a phone starts a WhatsApp voice call to this number. Embed it on websites, emails, or QR codes. Null while calling is disabled; not supported by WhatsApp desktop clients. |  [optional] |
|**forwardTo** | **String** | tel:+E164 / sip:... / wss://... destination |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**sipAuthUsername** | **String** |  |  [optional] |
|**sipAuthPasswordConfigured** | **Boolean** | True when a SIP digest password is stored. The plaintext is never returned. |  [optional] |
|**callIconCountries** | **List&lt;String&gt;** |  |  [optional] |
|**callerIdMode** | [**CallerIdModeEnum**](#CallerIdModeEnum) | Caller ID the forward-leg callee sees on tel: forwards. business &#x3D; this WhatsApp number; platform &#x3D; a Zernio number (customer-brought number without verified caller ID; verify via /v1/phone-numbers/{id}/whatsapp/caller-id-verification). |  [optional] |
|**callerIdVerified** | **Boolean** | True once the number completed caller-ID verification. |  [optional] |
|**maxCallDurationSeconds** | **Integer** | Hard cap (seconds) on forwarded calls; null &#x3D; no cap. |  [optional] |
|**forwardCallerId** | [**ForwardCallerIdEnum**](#ForwardCallerIdEnum) |  |  [optional] |



## Enum: CallerIdModeEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| PLATFORM | &quot;platform&quot; |



## Enum: ForwardCallerIdEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CALLER | &quot;caller&quot; |



