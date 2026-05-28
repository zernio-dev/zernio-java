

# GetWhatsAppCallingConfig200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumberDocId** | **String** | WhatsAppPhoneNumber Mongo ID (use on /v1/whatsapp/phone-numbers/{id}/calling) |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**callingEnabled** | **Boolean** |  |  [optional] |
|**forwardTo** | **String** | tel:+E164 / sip:... / wss://... destination |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**sipAuthUsername** | **String** |  |  [optional] |
|**sipAuthPasswordConfigured** | **Boolean** | True when a SIP digest password is stored. The plaintext is never returned. |  [optional] |
|**callIconCountries** | **List&lt;String&gt;** |  |  [optional] |



