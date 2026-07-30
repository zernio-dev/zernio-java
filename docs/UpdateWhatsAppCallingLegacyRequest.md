

# UpdateWhatsAppCallingLegacyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**forwardTo** | **String** |  |  [optional] |
|**sipAuthUsername** | **String** |  |  [optional] |
|**sipAuthPassword** | **String** |  |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**callIconCountries** | **List&lt;String&gt;** |  |  [optional] |
|**maxCallDurationSeconds** | **Integer** | Hard cap (seconds) on forwarded calls; null clears the cap. |  [optional] |
|**forwardCallerId** | [**ForwardCallerIdEnum**](#ForwardCallerIdEnum) | caller &#x3D; present the WhatsApp user&#39;s number to the forward destination (sip: only). |  [optional] |



## Enum: ForwardCallerIdEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CALLER | &quot;caller&quot; |



