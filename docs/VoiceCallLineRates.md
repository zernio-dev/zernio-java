

# VoiceCallLineRates


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**origination** | [**OriginationEnum**](#OriginationEnum) | Caller-ID band the carrier rates this call with. &#x60;unknown_caller&#x60; (no caller ID) shows the dearest band. |  [optional] |
|**perMinuteUsd** | **BigDecimal** | The rate most of this line type&#39;s networks share. |  [optional] |
|**minPerMinuteUsd** | **BigDecimal** |  |  [optional] |
|**maxPerMinuteUsd** | **BigDecimal** |  |  [optional] |
|**networks** | [**List&lt;VoiceCallLineRatesNetworksInner&gt;**](VoiceCallLineRatesNetworksInner.md) |  |  [optional] |



## Enum: OriginationEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;local&quot; |
| FROM_EEA | &quot;from_eea&quot; |
| NON_SURCHARGED | &quot;non_surcharged&quot; |
| LOW_SURCHARGED | &quot;low_surcharged&quot; |
| HIGH_SURCHARGED | &quot;high_surcharged&quot; |
| SURCHARGED | &quot;surcharged&quot; |
| DEFAULT | &quot;default&quot; |
| UNKNOWN_CALLER | &quot;unknown_caller&quot; |



