

# EnableWhatsAppCallingLegacyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**forwardTo** | **String** | tel:+E164 / sip:... / wss://... destination |  |
|**sipAuthUsername** | **String** |  |  [optional] |
|**sipAuthPassword** | **String** | Stored encrypted, never returned by any endpoint. |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**callIconCountries** | **List&lt;String&gt;** |  |  [optional] |
|**maxCallDurationSeconds** | **Integer** | Hard cap (seconds) on a forwarded call; the carrier hangs up both legs when it fires. Safety valve against dead-air billing when a destination hangs up but the signal is lost. |  [optional] |
|**forwardCallerId** | [**ForwardCallerIdEnum**](#ForwardCallerIdEnum) | Caller ID presented to the forward destination. caller &#x3D; the WhatsApp user&#39;s number (sip: destinations only; ignored on tel: forwards). Fixes AI-agent trunks that reject seeing the business number call itself. |  [optional] |



## Enum: ForwardCallerIdEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CALLER | &quot;caller&quot; |



