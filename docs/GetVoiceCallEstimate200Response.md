

# GetVoiceCallEstimate200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**via** | [**ViaEnum**](#ViaEnum) |  |  [optional] |
|**destinationCountry** | **String** | ISO country of &#x60;to&#x60;. Isle of Man, Jersey and Guernsey numbers return IM, JE and GG. |  [optional] |
|**lineType** | [**LineTypeEnum**](#LineTypeEnum) | Line type of &#x60;to&#x60;. Where it is not &#x60;mobile&#x60; or &#x60;landline&#x60;, &#x60;perMinuteUsd&#x60; takes the dearer of the two. |  [optional] |
|**callerId** | **String** | Caller ID the rates were picked for. Voice API estimates without &#x60;from&#x60; use your first calling number. |  [optional] |
|**callerCountry** | **String** |  |  [optional] |
|**minutes** | **Integer** |  |  [optional] |
|**perMinuteUsd** | **BigDecimal** | Billable cost per minute for &#x60;to&#x60;&#39;s line type and the requested options. |  [optional] |
|**billingIncrementSeconds** | [**GetVoiceCallEstimate200ResponseBillingIncrementSeconds**](GetVoiceCallEstimate200ResponseBillingIncrementSeconds.md) |  |  [optional] |
|**rates** | [**GetVoiceCallEstimate200ResponseRates**](GetVoiceCallEstimate200ResponseRates.md) |  |  [optional] |
|**trunk** | [**GetVoiceCallEstimate200ResponseTrunk**](GetVoiceCallEstimate200ResponseTrunk.md) |  |  [optional] |
|**breakdown** | [**GetVoiceCallEstimate200ResponseBreakdown**](GetVoiceCallEstimate200ResponseBreakdown.md) |  |  [optional] |



## Enum: ViaEnum

| Name | Value |
|---- | -----|
| TRUNK | &quot;trunk&quot; |
| VOICE | &quot;voice&quot; |



## Enum: LineTypeEnum

| Name | Value |
|---- | -----|
| MOBILE | &quot;mobile&quot; |
| LANDLINE | &quot;landline&quot; |
| FIXED_LINE_OR_MOBILE | &quot;fixed_line_or_mobile&quot; |
| OTHER | &quot;other&quot; |
| UNKNOWN | &quot;unknown&quot; |



