

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



