

# CreateVoiceCallRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**to** | **String** | Destination to dial, E.164 with leading +. |  |
|**fromNumber** | **String** | Which of your voice-enabled numbers to dial from. Optional when you have exactly one. |  [optional] |
|**forwardTo** | **String** | Per-call agent override (tel:+E164, sip:..., or wss://...); defaults to the number&#39;s stored forward destination. |  [optional] |
|**greeting** | **String** | Spoken to the callee when they answer, before the bridge. |  [optional] |
|**recordOverride** | **Boolean** | Per-call recording toggle; defaults to the number&#39;s setting. |  [optional] |
|**transcribeOverride** | **Boolean** | Per-call transcription toggle; defaults to the number&#39;s setting. |  [optional] |
|**transcriptionLanguage** | [**TranscriptionLanguageEnum**](#TranscriptionLanguageEnum) | &#39;auto&#39; derives from the callee&#39;s country; &#39;en&#39;/&#39;es&#39; force it. |  [optional] |
|**amd** | **Boolean** | Answering-machine detection; defers the bridge until human vs machine is known. |  [optional] |
|**voicemailDropMessage** | **String** | Spoken to a detected machine, then hang up (implies &#x60;amd&#x60;). For outbound voicemail drops. |  [optional] |



## Enum: TranscriptionLanguageEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| EN | &quot;en&quot; |
| ES | &quot;es&quot; |



